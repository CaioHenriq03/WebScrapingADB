call touch _____tmp.py 
call ipython -i _____tmp.py -c="run %1" --Completer.use_jedi=True --Completer.greedy=True --Completer.suppress_competing_matchers=True --Completer.limit_to__all__=False --Completer.jedi_compute_type_timeout=10000 --Completer.evaluation='dangerous' --Completer.auto_close_dict_keys=True --PlainTextFormatter.max_width=9999 --HistoryManager.hist_file=C:/Users/kaka_/ipython_hist.sqlite --HistoryManager.db_cache_size=0 --TerminalInteractiveShell.xmode='Verbose' --TerminalInteractiveShell.space_for_menu=20 --TerminalInteractiveShell.history_load_length=10000 --TerminalInteractiveShell.history_length=100000 --TerminalInteractiveShell.display_page=True --TerminalInteractiveShell.autoformatter='black' --TerminalInteractiveShell.auto_match=True --logappend=\=/ --logfile=\=/ --InteractiveShell.history_load_length=10000 --InteractiveShell.history_length=100000 --cache-size=100000 --BaseIPythonApplication.log_level=30 --colors=Linux 