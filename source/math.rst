数学原理
=========

loremremremrem

This is a test. Here is an equation:
:math:`X_{0:5} = (X_0, X_1, X_2, X_3, X_4)`.
Here is another:

.. math::
    :label: This is a label

    \nabla^2 f =
    \frac{1}{r^2} \frac{\partial}{\partial r}
    \left( r^2 \frac{\partial f}{\partial r} \right)


研究方法
=============

this is another math

step 1 第一步
--------------

this is a subtitle

.. code-block:: cpp

    void infer(cv::Mat &input_image, cv::Mat &output_image, cv::Mat &scores_matrix, cv::Mat &class_ids_matrix, MaskRCNN &model, std::shared_ptr<InferenceConfig> config, bool &IsMaskRCNNInferring) {
      IsMaskRCNNInferring = true;
      inference(input_image, output_image, scores_matrix, class_ids_matrix, model, config);
      IsMaskRCNNInferring = false;
      auto stop = std::chrono::steady_clock::now();
    }

    int main(int argc, char *argv[]) {
      // Set MaskRCNN Parameters
      std::string model_path = "/home/src/MaskFusion_cpp/model/mask_rcnn_coco.dat";
      cv::Mat input_image_bgr;
      cv::Mat output_image(480, 640, CV_8UC3, cv::Scalar(255,255,255));
      cv::Mat scores_matrix(480, 640, CV_32FC1, cv::Scalar(0.0));
      cv::Mat class_ids_matrix(480, 640, CV_32FC1, cv::Scalar(0.0));;
      bool IsMaskRCNNInferring = false;
      Eigen::Matrix4f mask_pose = Eigen::Matrix4f::Identity();

      auto config = std::make_shared<InferenceConfig>();
      std::string model_dir = "./";
      // Create model object.
      MaskRCNN model(model_dir, config);

      if (config->gpu_count > 0)
        model->to(torch::DeviceType::CUDA);

      std::tie(model, config) = model_prepare(model_path);

      caffe::Caffe::SetDevice(1);
      caffe::Caffe::set_mode(caffe::Caffe::GPU);