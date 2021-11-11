from verilog.verilog import VERILOGPlugin as VERILOG

def load_ipython_extension(ip):

    verilog_plugin = VERILOG(ip)
    ip.register_magics(verilog_plugin)
