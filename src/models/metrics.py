import tensorflow as tf
import keras.backend as K


def f1(y_true, y_pred):
    y_pred = K.round(y_pred)
    tp = K.sum(K.cast(y_true*y_pred, 'float'), axis=0)
    # tn = K.sum(K.cast((1-y_true)*(1-y_pred), 'float'), axis=0)
    fp = K.sum(K.cast((1-y_true)*y_pred, 'float'), axis=0)
    fn = K.sum(K.cast(y_true*(1-y_pred), 'float'), axis=0)

    p = tp / (tp + fp + K.epsilon())
    r = tp / (tp + fn + K.epsilon())

    f1 = 2*p*r / (p+r+K.epsilon())
    f1 = tf.where(tf.is_nan(f1), tf.zeros_like(f1), f1)
    #return K.mean(f1)

def evaluate_model(test_documents, test_labels, batch_size):
    # returns a
    score = model.evaluate(test_documents, test_labels,
                           batch_size=batch_size, verbose=1)

    predicted_labels = model.predict(test_documents, verbose=1)
    print(metrics.f1(test_labels, predicted_labels))
    # print('F1: ' + str(metrics.f1(test_labels, predicted_labels)))