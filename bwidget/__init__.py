import tkinter as tk
import os

class BWidget(tk.Widget):
    _bwidget_loaded = False

    def __init__(self, master, widget_name, cnf={}, **kw):
        if not BWidget._bwidget_loaded:
            bwidget_path = os.path.join(os.path.dirname(__file__))

            master.tk.eval('namespace eval ::BWIDGET {}')
            master.tk.eval(f'set ::BWIDGET::LIBRARY {{{bwidget_path}}}')

            core_files = ['widget.tcl', 'utils.tcl', 'themeutils.tcl', 'arrow.tcl', 'init.tcl']
            for file in core_files:
                master.tk.eval(f'source {{{os.path.join(bwidget_path, file)}}}')

            BWidget._bwidget_loaded = True

        tk_widget_name = f'BWidget::{widget_name}'
        if cnf:
            kw.update(cnf)
        tk.Widget.__init__(self, master, tk_widget_name, {}, kw)