import cv2
import numpy as np

# متغيرات عامة
initial_y, initial_x, k = 0, 0, 1

# دالة لما تدوس بالماوس على أي نقطة في الكاميرا
def onMouse(event, x, y, flags, param):
    global initial_y, initial_x, k
    if event == cv2.EVENT_LBUTTONDOWN:
        initial_x, initial_y = x, y
        k = -1
        print(f"Selected point: ({x}, {y})")  # ✅ يطبع مكان النقطة

# تشغيل الكاميرا الأولى لاختيار النقطة
cv2.namedWindow("Select Point")
cv2.setMouseCallback("Select Point", onMouse)
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow("Select Point", frame)
    if cv2.waitKey(1) == 27 or k == -1:  # ESC أو كليك ماوس
        old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cap.release()
        cv2.destroyAllWindows()
        break

# كاميرا جديدة للتتبع
cap1 = cv2.VideoCapture(0)
old_pts = np.array([[initial_x, initial_y]], dtype="float32").reshape(-1, 1, 2)
mask = np.zeros_like(frame)

while True:
    _, frame2 = cap1.read()
    new_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    # حساب الـ Optical Flow
    new_pts, status, err = cv2.calcOpticalFlowPyrLK(
        old_gray, new_gray, old_pts, None, maxLevel=1,
        criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 15, 0.008)
    )
    
    bn, cn = int(new_pts.ravel()[0]), int(new_pts.ravel()[1])
    print(f"Tracking point at: ({bn}, {cn})")  # ✅ يطبع مكان النقطة الحالي
    
    # رسم النقطة
    cv2.circle(mask, (bn, cn), 8, (0, 0, 255), -1)
    combined = cv2.addWeighted(frame2, 0.7, mask, 0.3, 0.1)
    
    # كتابة الإحداثيات على الصورة
    cv2.putText(combined, f"({bn}, {cn})", (bn + 10, cn - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    cv2.imshow("Tracking", combined)
    
    old_gray = new_gray.copy()
    old_pts = new_pts.copy()
    
    if cv2.waitKey(1) == 27:  # ESC للخروج
        cap1.release()
        cv2.destroyAllWindows()
        break
