        self.edi_loglist = []

# COMMAND ----------
myvars = vars()
try:
    if __name__ == "__main__":
        A = ods(cl_sk, cycle_sk)
        for key, value in myvars["functions_" + cl_sk].items():
            if value == None:
                a = eval("A." + key)()
            else:
                a = eval("A." + key)(value)

            if a == -1:
                break

        edi_cycle_log(A.edi_loglist, log_proc_name)

except:
    errortype = sys.exc_info()[0].__name__
    errorlineno = sys.exc_info()[2].tb_lineno
    errormessage = sys.exc_info()[1].args[0].replace("'", "")
    print(errormessage)

    A.edi_loglist.append(
        [
            gettimeStamp(),
            "Status",
            "***ERROR***",
            errortype,
            errorlineno,
            errormessage,
        ]
    )
    edi_cycle_log(A.edi_loglist, log_proc_name)
    raise errormessage
