tupla_prestazioni_operatori = (
    ("Milano", [
        ("gennaio", ("chiamateGestite", 320)),
        ("gennaio", ("oreLavorate", 160)),
        ("febbraio", ("chiamateGestite", 300)),
        ("febbraio", ("oreLavorate", 150)),
        ("aprile", ("chiamateGestite", 280)),
        ("aprile", ("oreLavorate", 140)),
        ("marzo", ("chiamateGestite", 260)),
        ("marzo", ("oreLavorate", 130)),
    ]),
    ("Roma", [
        ("gennaio", ("chiamateGestite", 350)),
        ("gennaio", ("oreLavorate", 170)),
        ("febbraio", ("chiamateGestite", 310)),
        ("febbraio", ("oreLavorate", 165)),
        ("aprile", ("chiamateGestite", 260)),
        ("aprile", ("oreLavorate", 160)),
        ("marzo", ("chiamateGestite", 220)),
        ("marzo", ("oreLavorate", 155)),
    ]),
    ("Firenze", [
        ("gennaio", ("chiamateGestite", 330)),
        ("gennaio", ("oreLavorate", 170)),
        ("febbraio", ("chiamateGestite", 310)),
        ("febbraio", ("oreLavorate", 160)),
        ("aprile", ("chiamateGestite", 290)),
        ("aprile", ("oreLavorate", 150)),
        ("marzo", ("chiamateGestite", 270)),
        ("marzo", ("oreLavorate", 140)),
    ]),
    ("Napoli", [
        ("gennaio", ("chiamateGestite", 400)),
        ("gennaio", ("oreLavorate", 200)),
        ("febbraio", ("chiamateGestite", 500)),
        ("febbraio", ("oreLavorate", 250)),
        ("aprile", ("chiamateGestite", 550)),
        ("aprile", ("oreLavorate", 255)),
        ("marzo", ("chiamateGestite", 450)),
        ("marzo", ("oreLavorate", 300)),
    ]),
)

analizza_prestazioni_operatori(tupla_prestazioni_operatori, "Milano", "chiamateGestite")