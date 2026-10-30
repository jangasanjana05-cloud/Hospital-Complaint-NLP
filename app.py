
import gradio as gr
from backend import predict_complaint

demo = gr.Interface(
    fn=predict_complaint,
    inputs=gr.Textbox(
        lines=4,
        label="Enter Hospital Complaint"
    ),
    outputs=[
        gr.Textbox(label="Predicted Complaint Category"),
        gr.Textbox(label="Predicted Priority")
    ],
    title="Hospital Complaint Classification and Priority Prediction Using NLP"
)

demo.launch()
