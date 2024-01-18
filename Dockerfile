FROM python:3.8
RUN pip install joblib streamlit pandas scikit-learn==1.2.2
COPY src/app.py /app/
COPY model/insurance_model.pkl /app/model/insurance_model.pkl
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]