import sys
from utils.log import Log


class CameraController:
    def __init__(self, p_env, p_camera_service, p_queue_service):
        self.env = p_env
        self.camera_service = p_camera_service
        self.queue_service = p_queue_service
        self.pending_pics = []

    def create(self):
        pic_names = self.camera_service.take_pictures()
        if len(self.pending_pics) != 0:
            self.queue_service.push(pic_names)
        self.pending_pics = pic_names
        base64_dict = {'photo1': {'id': pic_names[0],
                                  'content': self.camera_service.encode_image(pic_names[0])},
                       'photo2': {'id': pic_names[1],
                                  'content': self.camera_service.encode_image(pic_names[1])}
                       }
        return base64_dict

    def update(self):
        pic_names = self.camera_service.take_pictures()
        self.camera_service.delete_photos(self.pending_pics)
        self.pending_pics = pic_names
        base64_dict = {'photo1': {'id': pic_names[0],
                                  'content': self.camera_service.encode_image(pic_names[0])},
                       'photo2': {'id': pic_names[1],
                                  'content': self.camera_service.encode_image(pic_names[1])}
                       }
        return base64_dict

    def prepare_devices(self):
        try:
            self.camera_service.set_camera_config()
            self.camera_service.prepare_cams()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            log = Log()
            log.log_error('Error in the method set_new_project_config')
            return {'status': 1}  # Change to -1
        return {'status': 1}

    def delete(self):
        pass

    def stop_scanning(self):
        self.queue_service.wait_process()
        return {'ready': True}

    def get(self):
        pass
