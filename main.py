from jivago.jivago_application import JivagoApplication
import watch_party


app = JivagoApplication(watch_party)

if __name__ == '__main__':
    app.run_dev()
