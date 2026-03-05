import pickle
import pandas as pd

def main():
    with open("student_performance.pkl","rb") as f:
        saved_data = pickle.load(f)

    model = saved_data["model"]
    X_test_scaled = pd.read_csv("student_data_scaled.csv")
    print(model.predict(X_test_scaled))

if __name__ == "__main__":
    main()