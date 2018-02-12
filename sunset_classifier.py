import os
import urllib.request

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class SunsetClassifier(object):
    def __init__(self):
        # Loads label file, strips off carriage return
        self.label_lines = [line.rstrip() for line in tf.gfile.GFile("retrained_labels.txt")]

        # Unpersists graph from file
        with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')

    def classify(self, url):
        image_path, _ = urllib.request.urlretrieve(url)

        # Read in the image_data
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()

        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

            predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            buf = []
            for node_id in top_k:
                human_string = self.label_lines[node_id]
                score = predictions[0][node_id]
                buf.append('%s (score = %.5f)' % (human_string, score))
            return "\n".join(buf)
