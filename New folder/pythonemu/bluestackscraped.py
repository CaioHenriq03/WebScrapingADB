import re
import sys
from time import sleep
import pandas as pd
from PrettyColorPrinter import add_printer

add_printer(1)
from usefuladb import AdbControl
from lxml2pandas import subprocess_parsing

add_printer(1)

# To connect to all devices at once, you can use this static method (Windows only):
AdbControl.connect_to_all_tcp_devices_windows(
    adb_path=r"C:\adb\platform-tools\adb.exe",
)
# Blocking Shell
# - Waits until stderr/stdout have finished processing.
# - if you run "cd /sdcard/" and then another command "ls", for example, you will see the contents of /sdcard/.
# - If you switch to su, you will remain in the superuser mode.
# - Commands are not base64 encoded
addr = "127.0.0.1:5555"

eval_shell = AdbControl(
    adb_path=r"C:\adb\platform-tools\adb.exe",
    device_serial=addr,
    use_busybox=False,
    connect_to_device=True,
    invisible=True,
    print_stdout=False,
    print_stderr=True,
    limit_stdout=3,
    limit_stderr=3,  # limits the history of shellcommands - can be checked at blocking_shell.stderr
    limit_stdin=None,
    convert_to_83=True,
    wait_to_complete=0,
    flush_stdout_before=True,
    flush_stdin_before=True,
    flush_stderr_before=True,
    exitcommand="xxxCOMMANDxxxDONExxx",
    capture_stdout_stderr_first=True,
    global_cmd=True,
    global_cmd_timeout=10,
    use_eval=True,  # executes commands using eval
    eval_timeout=30,  # timeout for eval (netcat transfer)
)
df = eval_shell.get_all_activity_elements(as_pandas=True)
x, y = df.loc[df.ELEMENT_ID == "app:id/optional_toolbar_button"][
    ["CENTER_X", "CENTER_Y"]
].__array__()[0]


script ="""#!/bin/bash
cd /sdcard/Download
rm * -f

check_if_finished_writing() {
    timeout2=$(($SECONDS + timeoutfinal))

    while true; do
        if [ $SECONDS -gt "$timeout2" ]; then
            return 1
        fi
        initial_size=$(stat -c %s "$1")
        sleep "$2"
        current_size=$(stat -c %s "$1")
        if [ "$current_size" -eq "$initial_size" ]; then
            return 0
        fi
    done
}

while true; do
    input tap XCOORD YCOORD
    sleep 0.1
    file_contents=$(ls *.html -1 | tail -n 1)

    if [ -z "$file_contents" ]; then
        continue
    else
        if check_if_finished_writing "$file_contents" 0.1; then
            cat "$file_contents"
            rm * -f
        fi
    fi
    break
done""".replace("XCOORD", str(x)).replace("YCOORD", str(y))
while True:
    try:
        stdout,stderr=eval_shell.execute_sh_command(script)
        htmldata=[(x[0].decode(), x[1]) for x in
                    re.findall(br'<div><p>ELEMENTSEPSTART(\d+)</p></div>(.*?)<div><p>ELEMENTSEPEND\d+</p></div>'
                        , stdout[0])]

        df = subprocess_parsing(
            htmldata,
            chunks=1,
            processes=5,
            fake_header=True,
            print_stdout=False,
            print_stderr=True,
        )
        allelementsdf = df.loc[df.aa_attr_values == 'ovm-Fixture_Container']
        allframes = []
        for key, item in allelementsdf.iterrows():
            df2 = df.loc[df.aa_element_id.isin(item.aa_all_children) &
                            (df.aa_doc_id == item.aa_doc_id)]
            df3 = df2.loc[df2.aa_attr_values.isin(['ovm-ParticipantOddsOnly_Odds',
                                                    'ovm-FixtureDetailsTwoWay_TeamName'])]
            if len(df3) == 5:
                allframes.append(df3.aa_text.reset_index(drop=True).to_frame().T)
        dffinal = (pd.concat(allframes)).astype({2: 'Float64',
                                                3: 'Float64',4:
                                                    'Float64'}).reset_index(drop=True)
        print(dffinal)
    except Exception as e:
        sys.stderr.write(f'{e}\n')
        sys.stderr.flush()

