import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
import pandas as pd
#import numpy as np

def main():
    df = pd.read_csv('air.csv')

    y = df['scaled_sound'].as_matrix().reshape(-1,1)
    x = df.drop('scaled_sound',axis=1).as_matrix()

    x = preprocessing.scale(x)   # Divides by standard deviation and subtract mean

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

    x_ = tf.placeholder('float')
    y_ = tf.placeholder('float')

    '''
    keep_prob1 = tf.placeholder('float')  #For dropout
    keep_prob2 = tf.placeholder('float')  #For dropout
    '''
    #-------------------------------------------------------------------------------
    features = 5
    hidden_nodes_1 = 100
    hidden_nodes_2 = 10
    classes = 1
    epoch = 10000
    lambda_reg = 0.001

    #-------------------------------------------------------------------------------
    # Layers
    hidden_layer_1 = {'weights':tf.Variable(tf.random_uniform([features,hidden_nodes_1])),
                    'biases':tf.Variable(tf.random_uniform([hidden_nodes_1]))}

    hidden_layer_2 = {'weights':tf.Variable(tf.random_uniform([hidden_nodes_1,hidden_nodes_2])),
                    'biases':tf.Variable(tf.random_uniform([hidden_nodes_2]))}

    output_layer = {'weights':tf.Variable(tf.random_uniform([hidden_nodes_2,classes])),
                    'biases':tf.Variable(tf.random_uniform([classes]))}

    #-------------------------------------------------------------------------------
    l1 = tf.add(tf.matmul(x_,hidden_layer_1['weights']), hidden_layer_1['biases'])
    l1 = tf.nn.relu(l1)
    #l1 = tf.nn.dropout(l1,keep_prob1)

    l2 = tf.add(tf.matmul(l1,hidden_layer_2['weights']), hidden_layer_2['biases'])
    l2 = tf.nn.relu(l2)
    #l2 = tf.nn.dropout(l2,keep_prob2)

    output = tf.add(tf.matmul(l2,output_layer['weights']), output_layer['biases'])


    #-------------------------------------------------------------------------------
    regularisation = 0
    '''
    regularisation = lambda_reg*(tf.nn.l2_loss(hidden_layer_1['weights'])
                                    + tf.nn.l2_loss(hidden_layer_1['biases'])
                                    + tf.nn.l2_loss(hidden_layer_2['weights'])
                                    + tf.nn.l2_loss(hidden_layer_2['biases'])
                                    + tf.nn.l2_loss(output_layer['weights'])
                                    + tf.nn.l2_loss(output_layer['biases'])
                                    )
    '''
    #-------------------------------------------------------------------------------

    l1_regularizer = tf.contrib.layers.l1_regularizer(
       scale=0.005, scope=None
    )
    weights = tf.trainable_variables()
    regularisation = tf.contrib.layers.apply_regularization(l1_regularizer, weights)

    #-------------------------------------------------------------------------------
    error = tf.reduce_mean(tf.square(output-y_)+ regularisation)

    #train = tf.train.GradientDescentOptimizer(0.0001).minimize(error)
    train = tf.train.AdamOptimizer(0.01).minimize(error)

    per_error = tf.reduce_mean(abs(output-y_)/y_)*100   #For testing data

    #-------------------------------------------------------------------------------
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(epoch):
            _,e = sess.run([train,error],feed_dict= {x_:x_train,y_:y_train
                                                            #, keep_prob1:0.75
                                                            #, keep_prob2:0.75
                                                            })
            if i%100==0:
                print('Epoch : ',i+1,'Error : ',e)

        output,Testing_error = sess.run([output,per_error],feed_dict={x_:x_test,y_:y_test
                                                                        #,keep_prob1:1.0
                                                                        #,keep_prob2:1.0
                                                                        })

        #--------------------------------Printing the true value and predicted value
        '''
        for i in range(len(y_test)):
                #print(y_test[i],output[i])
        '''
        #-------------------------------------Calculating testing error for accuracy
        print('Testing_error : ',Testing_error)

        #-------------------------------------------------------------Plotting data
        plt.plot(range(len(y_test)),y_test,'g',label = 'Actual Data')
        plt.plot(range(len(y_test)),output,'r--',label = 'predicted data')
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)
        #plt.axis([100, 150,100, 140])
        plt.grid(True)
        plt.show()

