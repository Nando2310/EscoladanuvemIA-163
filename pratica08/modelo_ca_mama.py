# Importação das bibliotecas do projeto
from sklearn.datasets import load_breast_cancer # Dataset de CA de mama
from sklearn.ensemble import RandomForestClassifier # Algoritimo Random Forest

# Metricas para avaliação do modelo
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

# Função para dividir o conjunto de dados 
from sklearn.model_selection import train_test_split

# Carregar o dataset de CA de mama
data = load_breast_cancer()

"""
O dataset possui caracteristicas (data.data) e rotulos (data.target).
data.data: Matriz com as 30 caracteristicas para cada uma das amostras
data.target: vetor 0 (maligno) ou 1 (benigno) para cada amostra
Dividir os dados em conjuntos de treino (70%) e de teste (30%).
x_train e x_test: caracteristicas de treino e de teste
y_train e y_test: rotolus para treino e teste
random_state=42, garantir que a reprodutibilidade dos resultados
"""

x_train, x_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42
)

# Iniciar o modelo com os parametros padrão
model = RandomForestClassifier()

# Treinamento do modelo
model.fit(x_train,y_train)

# Previsão do modelo com os dados de teste
y_pred = model.predict(x_test)
y_pred_proba = model.predict_proba(x_test)[:,1]

# Calculo das metricas de avaliação
precision = precision_score(y_test, y_pred) #Precisão TP / (TP + FP)
recall = recall_score(y_test, y_pred) # Recall TP / (TP + FN)
f1 = f1_score(y_test, y_pred) # F1 Score: 2*(precision*recall) / (precision*recall) 
auc = roc_auc_score(y_test, y_pred) # Area da curva ROC

print(f"A metrica precision é: {precision:.2f}")
print(f"A metrica Recall é: {recall:.2f}")
print(f"A metrica f é: {f1:.2f}")
print(f"A metrica auc é: {auc:.2f}")
