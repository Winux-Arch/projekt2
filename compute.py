def plot_formula(formula, domain):
    """
    formula: eingegebene Formel
    domain: Bereich zum plotten
    """
    # Ausrechnen des Intervalls und extrahieren von xmin und xmax.
    # Ausrechnung in numpy namespace dass Intervall '[0, pi/2]' als mögliche Spezifikation.
    import numpy as np
    import base64
    from io import BytesIO
    import matplotlib.figure as plt
    #Error catcher
    input_error = False
    try:
        domain_list = eval(domain, np.__dict__)
        xmin, xmax = domain_list
    except Exception as e:
        input_error = True
    if not isinstance(domain, list) and len(domain) == 2:
        input_error = True
    if input_error:
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
    

    # Definieren der x Koordinaten
    x = np.linspace(xmin, xmax, 10001)
    # Ändert Formel in einen numpy-akzeptierten Ausdruck
    # np.__dict__ namespace und x müssen definiert sein, sonst wird Fehler angezeigt
    namespace = np.__dict__.copy()
    namespace.update({'x': x})
    try:
        y = eval(formula, namespace)
    except Exception as e:
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
    ax.plot(x,y)
    # Temporäres Speichern
    buf = BytesIO()
    fig.savefig(buf, format="png")
    figdata_png = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    return figdata_png
