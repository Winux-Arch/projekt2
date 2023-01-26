def plot_formula(formula, domain):
    """
    formula: eingegebene Formel
    domain: Bereich zum plotten
    """
    #Importierungen
    import numpy as np
    import base64
    from io import BytesIO
    import matplotlib.figure as plt
    #Error catcher
    input_error = False
    try:
        domain_list = eval(domain, np.__dict__)
        # Definieren der x Koordinaten
        xmin, xmax = domain_list
        x = np.linspace(xmin, xmax, 10001)
    except Exception as e:
        input_error = True
    if not isinstance(domain, list) or not len(domain) == 2:
        input_error = True
    if input_error:
        #erzeugt Fehlermeldung
        fig = plt.Figure()
        ax = fig.subplots()
        ax.plot([1,1])
        ax.text(0, 1, 'Fehler: Inkorrektes Intervall!', style='normal', bbox={
        'facecolor': 'red', 'alpha': 1, 'pad': 30})
        # Temporäres Speichern
        buf = BytesIO()
        fig.savefig(buf, format="png")
        figdata_png = base64.b64encode(buf.getbuffer()).decode("ascii")
        return figdata_png
    try:  
      # Ändert Formel in einen numpy-akzeptierten Ausdruck
      # np.__dict__ namespace und x müssen definiert sein, sonst wird Fehler angezeigt
      namespace = np.__dict__.copy()
      namespace.update({'x': x})
      y = eval(formula, namespace)
    except Exception as e:
        #zeigt Fehlermeldung
        fig = plt.Figure()
        ax = fig.subplots()
        ax.plot([1,1])
        ax.text(0, 1, 'Fehler: Inkorrekter Ausdruck!', style='normal', bbox={
        'facecolor': 'red', 'alpha': 1, 'pad': 30})
        # Temporäres Speichern
        buf = BytesIO()
        fig.savefig(buf, format="png")
        figdata_png = base64.b64encode(buf.getbuffer()).decode("ascii")
        return figdata_png
    # Plotten des Graphen
    fig = plt.Figure()
    ax = fig.subplots()
    ax.grid()
    ax.plot(x,y)
    # Temporäres Speichern
    buf = BytesIO()
    fig.savefig(buf, format="png")
    figdata_png = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    return figdata_png
