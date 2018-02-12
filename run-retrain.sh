#usage: retrain.py [-h] [--image_dir IMAGE_DIR] [--output_graph sunsetclassifier.pb]
#                  [--output_labels OUTPUT_LABELS]
#                  [--summaries_dir SUMMARIES_DIR]
#                  [--how_many_training_steps HOW_MANY_TRAINING_STEPS]
#                  [--learning_rate LEARNING_RATE]
#                  [--testing_percentage TESTING_PERCENTAGE]
#                  [--validation_percentage VALIDATION_PERCENTAGE]
#                  [--eval_step_interval EVAL_STEP_INTERVAL]
#                  [--train_batch_size TRAIN_BATCH_SIZE]
#                  [--test_batch_size TEST_BATCH_SIZE]
#                  [--validation_batch_size VALIDATION_BATCH_SIZE]
#                  [--print_misclassified_test_images] [--model_dir MODEL_DIR]
#                  [--bottleneck_dir BOTTLENECK_DIR]
#                  [--final_tensor_name FINAL_TENSOR_NAME] [--flip_left_right]
#                  [--random_crop RANDOM_CROP] [--random_scale RANDOM_SCALE]
#                  [--random_brightness RANDOM_BRIGHTNESS]

python retrain.py --output_graph retrained_graph.pb --output_labels retrained_labels.txt --image_dir data/train/ --how_many_training_steps 100

