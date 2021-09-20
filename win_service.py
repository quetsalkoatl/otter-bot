import win32serviceutil
import win32service
from multiprocessing import Process

import otter_bot


class OtterBotSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "OtterBotService"
    _svc_display_name_ = "Otter Bot Service"

    def __init__(self, *args):
        super().__init__(*args)
        self.process = Process(target=self.main)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.process.terminate()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def SvcDoRun(self):
        self.process.start()
        self.process.run()

    def main(self):
        otter_bot.main()


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(OtterBotSvc)
