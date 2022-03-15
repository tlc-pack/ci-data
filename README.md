This repo is used to house binary files used in [TVM's](https://github.com/apache/tvm) Jenkins [CI](https://ci.tlcpack.ai).

To add a file to this repo, send a PR with:

1. The file itself. For example:
    ```bash
    cd files
    curl -LO https://github.com/tensorflow/tflite-micro/raw/main/tensorflow/lite/micro/examples/micro_speech/micro_speech.tflite
    ```
2. An entry into [`files.json`](files.json) and run `python validate.py` to insert an entry into the table below
    ```bash
    pip install -r requirements.txt
    python validate.py
    git add .
    ```

| Filename | Source URL |
| -------- | ---------- |
| [`micro_speech.tflite`](files/micro_speech.tflite) | https://github.com/tensorflow/tflite-micro/raw/main/tensorflow/lite/micro/examples/micro_speech/micro_speech.tflite |
| [`mnist.tflite`](files/mnist.tflite) | https://storage.googleapis.com/download.tensorflow.org/models/tflite/digit_classifier/mnist.tflite |
| [`keyword_spotting_quant.tflite`](files/keyword_spotting_quant.tflite) | https://github.com/tlc-pack/web-data/raw/25fe99fb00329a26bd37d3dca723da94316fd34c/testdata/microTVM/model/keyword_spotting_quant.tflite |
| [`keyword_spotting_int8_6.pyc.npy`](files/keyword_spotting_int8_6.pyc.npy) | https://github.com/tlc-pack/web-data/raw/967fc387dadb272c5a7f8c3461d34c060100dbf1/testdata/microTVM/data/keyword_spotting_int8_6.pyc.npy |
| [`mnist_model_quant.tflite`](files/mnist_model_quant.tflite) | https://github.com/tlc-pack/web-data/raw/b2f3c02427b67267a00fd968ba1fce28fc833028/testdata/microTVM/model/mnist_model_quant.tflite |
| [`bertsquad-10.onnx`](files/bertsquad-10.onnx) | https://github.com/onnx/models/raw/bd206494e8b6a27b25e5cf7199dbcdbfe9d05d1c/text/machine_comprehension/bert-squad/model/bertsquad-10.onnx |
| [`mobilenetv2-7.onnx`](files/mobilenetv2-7.onnx) | https://github.com/onnx/models/raw/bd206494e8b6a27b25e5cf7199dbcdbfe9d05d1c/vision/classification/mobilenet/model/mobilenetv2-7.onnx |
| [`resnet50-v1-7.onnx`](files/resnet50-v1-7.onnx) | https://github.com/onnx/models/raw/bd206494e8b6a27b25e5cf7199dbcdbfe9d05d1c/vision/classification/resnet/model/resnet50-v1-7.onnx |
| [`resnet50-v2-7.onnx`](files/resnet50-v2-7.onnx) | https://github.com/onnx/models/raw/bd206494e8b6a27b25e5cf7199dbcdbfe9d05d1c/vision/classification/resnet/model/resnet50-v2-7.onnx |
| [`squeezenet1.1-7.onnx`](files/squeezenet1.1-7.onnx) | https://github.com/onnx/models/raw/bd206494e8b6a27b25e5cf7199dbcdbfe9d05d1c/vision/classification/squeezenet/model/squeezenet1.1-7.onnx |
| [`squeezenet1.0-7.onnx`](files/squeezenet1.0-7.onnx) | https://github.com/onnx/models/raw/bd206494e8b6a27b25e5cf7199dbcdbfe9d05d1c/vision/classification/squeezenet/model/squeezenet1.0-7.onnx |
| [`inception-v1-7.onnx`](files/inception-v1-7.onnx) | https://github.com/onnx/models/raw/bd206494e8b6a27b25e5cf7199dbcdbfe9d05d1c/vision/classification/inception_and_googlenet/inception_v1/model/inception-v1-7.onnx |
| [`inception-v2-7.onnx`](files/inception-v2-7.onnx) | https://github.com/onnx/models/raw/bd206494e8b6a27b25e5cf7199dbcdbfe9d05d1c/vision/classification/inception_and_googlenet/inception_v2/model/inception-v2-7.onnx |