# Sunset Classifier

## Training the Classifier
### `data/` structure
The training data is stored in `data/train/`. Inside this directory, add a
directory for every label you want to classify. In this case, we're simply
labeling `sunset` or `notsunset`.

Example:
```
data/train/notsunset/2018-02-09-17-55-51_thumb.jpg
data/train/notsunset/2018-02-09-21-03-50_thumb.jpg
data/train/notsunset/2018-02-09-22-38-29_thumb.jpg
...
data/train/sunset/2018-02-10-02-01-34_thumb.jpg
data/train/sunset/2018-02-10-01-56-35_thumb.jpg
data/train/sunset/2018-02-10-01-57-33_thumb.jpg
```

The validation set should follow the same structure in `data/val/`:
```
data/val/notsunset/2018-02-09-00-42-30_thumb.jpg
data/val/notsunset/2018-02-09-14-33-49_thumb.jpg
data/val/notsunset/2018-02-09-02-35-56_thumb.jpg
...
data/val/sunset/2018-02-09-02-00-22_thumb.jpg
data/val/sunset/2018-02-09-01-42-37_thumb.jpg
data/val/sunset/2018-02-09-02-06-24_thumb.jpg
```

To train the classifier on this data, use `run-retrain.sh`.


## Using the Classifier

```sh
$ python label_image.py data/train/sunset/2018-02-10-02-01-34_thumb.jpg
sunset (score = 0.99617)
notsunset (score = 0.00383)
```
