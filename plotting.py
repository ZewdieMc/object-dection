import matplotlib.pyplot as plt

# Data
epochs = list(range(1, 37))
train_loss = [2.8788, 1.2406, 1.1494, 1.1625, 1.1557, 1.1479, 1.1315, 1.1341, 1.1259, 1.4350, 
              1.1268, 1.1260, 1.1263, 1.1249, 1.0784, 0.8751, 0.5962, 0.5560, 0.8718, 0.5368, 
              0.5198, 0.4507, 0.0770, 0.0488, 0.0993, 0.0805, 0.0392, 0.0518, 0.0374, 0.0943, 
              0.0341, 0.0262, 0.0236, 0.0189, 0.0207, 0.0186]
val_loss = [1.5528, 1.1252, 1.1123, 1.1329, 1.2673, 1.1286, 1.1121, 1.1117, 1.1139, 1.1122, 
            1.1124, 1.1120, 1.1118, 1.1121, 0.9708, 0.6013, 0.5245, 0.5477, 0.5258, 0.5471, 
            0.4929, 0.1225, 0.0362, 0.0386, 0.0553, 0.1274, 0.0325, 0.0348, 0.2640, 0.0395, 
            0.0275, 0.0239, 0.0218, 0.0143, 0.0136, 0.0146]
train_acc = [0.3404, 0.3204, 0.3386, 0.3268, 0.3372, 0.3344, 0.3288, 0.3282, 0.3332, 0.3266, 
             0.3336, 0.3376, 0.3250, 0.3424, 0.4196, 0.5526, 0.6466, 0.6550, 0.6294, 0.6552, 
             0.6666, 0.7690, 0.9774, 0.9858, 0.9760, 0.9806, 0.9876, 0.9854, 0.9886, 0.9814, 
             0.9888, 0.9934, 0.9950, 0.9968, 0.9964, 0.9964]
val_acc = [0.3320, 0.3270, 0.3310, 0.3670, 0.3290, 0.3310, 0.3450, 0.3330, 0.3330, 0.3340, 
           0.3340, 0.3340, 0.3350, 0.4300, 0.5130, 0.6380, 0.6580, 0.6490, 0.6560, 0.6570, 
           0.6610, 0.9720, 0.9870, 0.9850, 0.9850, 0.9660, 0.9850, 0.9860, 0.9540, 0.9840, 
           0.9930, 0.9940, 0.9940, 0.9980, 0.9970, 0.9950]

# Plotting
plt.figure(figsize=(12, 8))

# Loss plot
plt.subplot(2, 1, 1)
plt.plot(epochs, train_loss, label='Train Loss', color='blue')
plt.plot(epochs, val_loss, label='Validation Loss', color='orange')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# Accuracy plot
plt.subplot(2, 1, 2)
plt.plot(epochs, train_acc, label='Train Accuracy', color='blue')
plt.plot(epochs, val_acc, label='Validation Accuracy', color='orange')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()
