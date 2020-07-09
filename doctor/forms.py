
def output(input_text):
    import numpy as np
    from tensorflow.keras.utils import to_categorical  # y변수 전처리
    from tensorflow.keras import Sequential  # model 생성
    from tensorflow.keras.layers import Dense
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.preprocessing import LabelEncoder
    import pandas as pd

    def clean_text(text):
        from re import sub
        texts_re = text.lower()  # 소문자 변경
        texts_re2 = sub('[0-9]', '', texts_re)  # 숫자 제거
        texts_re3 = sub('[.,;:?!]', '', texts_re2)  # 문장부호 제거
        texts_re4 = sub('[-@#$%^&*(){}]', '', texts_re3)  # 특수문자 제거
        texts_re5 = texts_re4.replace('\par', ' ')
        texts_re6 = texts_re5.replace('\\b', ' ')
        texts_re7 = texts_re6.replace('\\fs', ' ')
        texts_re8 = texts_re7.replace('/', ' ')
        texts_re8 = texts_re8.replace('[]', ' ')
        texts_re9 = ' '.join(texts_re8.split())  # 공백 제거
        return texts_re9

    x_test = clean_text(input_text)
    # 1. csv file read
    doctor_150 = pd.read_csv('D:/ITWILL/project/data/doctor_test.csv')
    target = doctor_150['CODE_DESCRIPTION']
    texts = doctor_150['NOTES']

    x_test = pd.Series(x_test)
    texts = texts.append(x_test)

    # 2. target -> 전처리 -> dummy 변수
    y_name = target.unique()
    y_name.sort()
    y_data = LabelEncoder().fit_transform(target)

    # 3. Sparse matrix
    sparse_mat = TfidfVectorizer(stop_words='english', max_features=8000).fit_transform(texts)

    # scipy -> numpy
    x_data = sparse_mat.toarray()
    x_train = x_data[:7613]
    x_test = x_data[-1]
    x_test = x_test.reshape(1, 8000)

    # list -> numpy
    y_data = np.array(y_data)
    y_data = y_data.reshape(-1, 1)
    y_data = to_categorical(y_data)

    ##### DNN model layer #####
    model = Sequential()
    model.add(Dense(128, activation='relu'))  # 1층
    model.add(Dense(64, activation='relu'))  # 2층
    model.add(Dense(24, activation='softmax'))  # 3층

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(x=x_train, y=y_data, epochs=5, validation_data=(x_train, y_data))

    ##### output 구현 #####
    pred = model.call(x_test)
    pred = np.round((pred[0] / sum(pred[0]))*100, 3)

    y_pred = pd.DataFrame(pred, y_name)
    y_pred = y_pred.sort_values([0], ascending=[False])
    top3 = y_pred[:3]
    return top3

'''
['Asthma', 'Bronchitis', 'Dermatitis', 'GORD', 'Hyperlipidaemia',
       'Hypertension', 'Immunisation', 'Immunisation, Influenza',
       'Influenza Immunisation', 'Iron deficiency anaemia', 'LRTI',
       'Obesity', 'Osteoarthritis', 'Otitis media', 'Pharyngitis',
       'Pregnancy', 'Sinusitis', 'Tonsillitis', 'URTI', 'URTI, bacterial',
       'URTI, viral', 'UTI', 'Viral illness', 'Vitamin D deficiency']
'''