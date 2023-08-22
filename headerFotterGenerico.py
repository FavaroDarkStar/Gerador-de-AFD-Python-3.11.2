def headerFotterGenerico():
    headerREF1 = "000000000"
    headerREF2 = "1"
    headerREF3 = "1"
    headerREF4 = "00455458000135"  # "CNPJ UNIDADE"
    headerREF5 = "            "  # "CNO CAEPF"
    headerREF6 = "GERADOR AFD FAVARO                                                                                                                                    "  # "RAZ SOC EMPREGADOR"
    nsREP = "00004004330107028"
    headerREF7 = nsREP+"2605202114042023140420231059868F"
    header = headerREF1 + headerREF2 + headerREF3 + headerREF4 + headerREF5 + headerREF6 + headerREF7
    fotter = "9999999990000000020000052270000000000000000630000000499"
    return [header, fotter]
