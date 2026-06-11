<h1 align="center">✋ Real-Time Hand Tracking</h1>
<h3 align="center">Lucas-Kanade Optical Flow Implementation</h3>

<hr/>

<h2>🚀 Project Overview</h2>
<p>
This project implements real-time hand tracking using the 
Lucas-Kanade Optical Flow algorithm in OpenCV.
</p>

<p>
Instead of traditional object detection, this system tracks motion 
between consecutive frames using feature point tracking.
</p>

<hr/>

<h2>🧠 Algorithm Used</h2>

<ul>
<li>Shi-Tomasi Corner Detection (Good Features to Track)</li>
<li>Lucas-Kanade Optical Flow</li>
<li>Frame-to-frame motion estimation</li>
<li>Feature point visualization</li>
</ul>

<hr/>

<h2>📊 How It Works</h2>

<ol>
<li>Capture video stream from webcam</li>
<li>Convert frame to grayscale</li>
<li>Detect strong feature points</li>
<li>Track their movement using Optical Flow</li>
<li>Draw motion vectors in real-time</li>
</ol>

<hr/>

<h2>📂 Project Structure</h2>

<pre>
hand-tracking-optical-flow-opencv/
│
├── hand_tracking_using_Lucas_Kanade.py
├── README.md
└── requirements.txt
</pre>

<hr/>

<h2>⚙️ How to Run</h2>

<pre>
pip install -r requirements.txt
python hand_tracking_using_Lucas_Kanade.py
</pre>

Press <b>q</b> to exit.

<hr/>

<h2>🛠 Requirements</h2>

<pre>
opencv-contrib-python
numpy
</pre>

<hr/>

<h2>💡 Engineering Highlights</h2>

<ul>
<li>Motion-based object tracking</li>
<li>Optical Flow implementation</li>
<li>Real-time feature point tracking</li>
<li>Classical Computer Vision techniques</li>
</ul>

<hr/>

<h2>🔮 Future Improvements</h2>

<ul>
<li>Integrate hand gesture recognition</li>
<li>Add trajectory smoothing</li>
<li>Combine with deep learning hand detection</li>
<li>Upgrade to MediaPipe Hands</li>
</ul>

<hr/>

<div align="center">
<h3>👨‍💻 Developed by abdelkreem abdelhaleem frahat</h3>
<p>AI Engineer | Computer Vision | Motion Tracking</p>
</div>
