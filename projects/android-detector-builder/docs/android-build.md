# Android build inputs

Copy the example manifest to a new model directory and put the indicated NCNN files next to it. The model must match the YOLOv8 layout and the input size expected by the native decoder. A header check confirms the parameter file format. It cannot verify compatibility with the decoder or the supplied class order.

Use an Android template with `app/src/main/jni/yolov8ncnn.cpp`, the `coco_names_en/es/it` arrays and the `model_array` string resource used by the original builder. The unmodified upstream template may need those resources and label arrays before it can be used. Supply the template with its NCNN and OpenCV Mobile dependencies, the matching Android SDK/NDK, and the JDK used by its Gradle wrapper. Build into a temporary workspace and keep the source template untouched.

Export the variables in [the example configuration](../config/base.env.example) if your SDK and JDK are not already configured. Use `--offline` when the required Gradle dependencies and SDK components are cached.
