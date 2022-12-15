from ..scanner import Scanner, Addr
from .. import resources
import logging
import cv2

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


mod_path = __file__
def test_avaliable(rtsp_url, threshold=10):
    vid = cv2.VideoCapture(rtsp_url)
    if not vid.isOpened():
        return False
    fail_cnt = 0
    while(fail_cnt<threshold):
        try:
            _, frame = vid.read()
            return True
        except KeyboardInterrupt:
            break
        except Exception as e:
            logging.debug(e)
            fail_cnt+=1
    return False

class RtspScanner(Scanner):
    name = 'rtsp scanner'
    protocol = 'rtsp'
    threshold = 10

    def __init__(
            self,
            debug=False
    ):
        super().__init__(debug)

    def check(self, addr: Addr) -> bool:
        return True

    def scan(self, addr: Addr, dictionary=None):
        if dictionary is None:
            trylist = pkg_resources.read_text(resources, 'rtsp_try.txt').splitlines()
        else:
            trylist = open(dictionary).read().splitlines()
        for line in trylist:
            rtsp_url = f'rtsp://{addr.address}:{addr.port}/{line.strip()}'
            if test_avaliable(rtsp_url):
                print(f'rtsp url found:')
                print(rtsp_url)
                return rtsp_url
        return None

    def view(self, rtsp_url, threshold=10):
        vid = cv2.VideoCapture(rtsp_url)
        if not vid.isOpened():
            print('rtsp url is not valid')
            return
        fail_cnt = 0
        while fail_cnt < threshold:
            try:
                _, frame = vid.read()
                cv2.imshow('Footage', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)
                fail_cnt += 1
        vid.release()
        cv2.destroyAllWindows()

    def capture(self, rtsp_url, output_path='output.png'):
        vid = cv2.VideoCapture(rtsp_url)
        if not vid.isOpened():
            print('rtsp url is not valid')
            return
        for _ in range(self.threshold):
            try:
                _, frame = vid.read()
                cv2.imwrite('capture.jpg', frame)
                break
            except KeyboardInterrupt:
                break
            except Exception as e:
                logging.debug(e)
        vid.release()
        cv2.destroyAllWindows()
