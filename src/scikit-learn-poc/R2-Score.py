from sklearn.metrics import r2_score

y_true = [1,2,4]
y_pred = [1.1,2.1,4.1]
y_pred_bad = [1,2,3.5]

print r2_score(y_true, y_pred)
print r2_score(y_true, y_pred_bad)