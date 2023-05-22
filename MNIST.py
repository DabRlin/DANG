# 导入所需的库和模块
from keras.utils import to_categorical
from keras import models, layers
from keras.optimizers import RMSprop
from keras.datasets import mnist

# 加载MNIST数据集，将其分为训练集和测试集
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 搭建LeNet网络模型
def LeNet():
    network = models.Sequential()
    # 添加第一个卷积层，包括6个过滤器，每个过滤器大小为3x3，激活函数为ReLU，并指定输入形状为28x28x1
    network.add(layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    # 添加第一个平均池化层，池化窗口大小为2x2
    network.add(layers.AveragePooling2D((2, 2)))
    # 添加第二个卷积层，包括16个过滤器，每个过滤器大小为3x3，激活函数为ReLU
    network.add(layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
    # 添加第二个平均池化层，池化窗口大小为2x2
    network.add(layers.AveragePooling2D((2, 2)))
    # 添加第三个卷积层，包括120个过滤器，每个过滤器大小为3x3，激活函数为ReLU
    network.add(layers.Conv2D(filters=120, kernel_size=(3, 3), activation='relu'))
    # 将特征图展平为一维向量
    network.add(layers.Flatten())
    # 添加第一个全连接层，包含84个神经元，激活函数为ReLU
    network.add(layers.Dense(84, activation='relu'))
    # 添加输出层，包含10个神经元，激活函数为softmax
    network.add(layers.Dense(10, activation='softmax'))
    return network

# 创建LeNet网络实例
network = LeNet()
# 配置网络模型，使用RMSprop优化器，学习率为0.001，损失函数为分类交叉熵，评估指标为准确率
network.compile(optimizer=RMSprop(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# 数据预处理：将图像数据reshape为合适的形状，进行归一化处理；将标签数据进行独热编码转换
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# 使用fit函数训练网络，设置训练轮次为10，批量大小为128，verbose参数为2表示显示训练过程中的进度信息
network.fit(train_images, train_labels, epochs=10, batch_size=128, verbose=2)

#在测试集上评估网络性能
test_loss, test_accuracy = network.evaluate(test_images, test_labels)

#打印测试集上的损失值和准确率
print("test_loss:", test_loss, " test_accuracy:", test_accuracy)