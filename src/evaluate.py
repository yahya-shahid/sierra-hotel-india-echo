import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, classification_report

model = load_model("models/crop_disease_cnn.h5")

test_gen = ImageDataGenerator(rescale=1/255.0)
test_data = test_gen.flow_from_directory(
    "data/test", target_size=(128,128), batch_size=32, class_mode='categorical', shuffle=False
)

y_true = test_data.classes
y_pred = np.argmax(model.predict(test_data), axis=1)

print(classification_report(y_true, y_pred))
print(confusion_matrix(y_true, y_pred))
