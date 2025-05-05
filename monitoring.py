import evidently
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import pandas as pd
# Charger les anciennes et nouvelles données
df_old = pd.read_csv("data/old_data.csv")
df_new = pd.read_csv("data/new_data.csv")
# Générer un rapport de Data Drift
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=df_old, current_data=df_new)
# Sauvegarder le rapport en HTML
report.save_html("report.html")
print("Rapport généré : report.html")