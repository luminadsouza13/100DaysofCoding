# Implement CORS
# learn same domain policy
# https://www.youtube.com/watch?v=Ka8vG5miErk

import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin","*")
        self.write(f"Hello Lumina")


def make_app():
    return tornado.web.Application([(r"/", MainHandler)])


if __name__ == "__main__":
    app = make_app()
    app.listen(8880)
    tornado.ioloop.IOLoop.current().start()
