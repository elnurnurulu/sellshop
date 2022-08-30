from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
import logging



class LogginMiddleware(MiddlewareMixin):

    def process_request(self,request):

        root_logger= logging.getLogger()
        root_logger.setLevel(logging.INFO) # or whatever
        handler = logging.FileHandler('test.log', 'w', 'utf-8') # or whatever
        handler.setFormatter(logging.Formatter('%(name)s %(message)s')) # or whatever
        root_logger.addHandler(handler)

        logging.info("Request Method : "+str(request.META["REQUEST_METHOD"]))
        logging.info("URL Requested : "+str(request.path))
        logging.info("Request Body Contents : "+str(request.body))
        # logging.info("Content Length : "+str(request.META["CONTENT_LENGTH"]))
        logging.info("Client IP Address : "+str(request.META["REMOTE_ADDR"]))
        # logging.info("Host Name of CLient : "+str(request.META["REMOTE_HOST"]))
        logging.info("Host Name of the Server : "+str(request.META["SERVER_NAME"]))
        logging.info("Port of the Server : "+str(request.META["SERVER_PORT"]))       
        return None

  

class BlockIPMiddleware(MiddlewareMixin):
    BLACKLIST =[
        # '192.168.88.49',
    ]

    def process_view(self, request, *args, **kwargs):
        # print(request.META['REMOTE_ADDR'] )

        if request.META['REMOTE_ADDR'] in self.BLACKLIST:
            return HttpResponseForbidden()


class ForceDefaultLanguageMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        if "HTTP_ACCEPT_LANGUAGE" in request.META:
            del request.META["HTTP_ACCEPT_LANGUAGE"]