class DashboardController:
        
    def __init__(self) -> None:
        pass
    
    def index(self, request):
        return 'DashboardController: index'

    def dashboardStatistics(self, request):
        return 'DashboardController: dashboardStatistics'

    def yearlyIncomeCountStat(self, request):
        return 'DashboardController: yearlyIncomeCountStat'
