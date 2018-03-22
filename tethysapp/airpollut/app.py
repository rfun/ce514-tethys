from tethys_sdk.base import TethysAppBase, url_map_maker


class Airpollut(TethysAppBase):
    name = 'Air Quality Prediction'
    index = 'airpollut:home'
    icon = 'airpollut/images/icon.gif'
    package = 'airpollut'
    root_url = 'airpollut'
    color = '#64b5f6'
    description = 'Monitor Air Quality in your neighborhood'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='airpollut',
                controller='airpollut.controllers.home'
            ),
            UrlMap(
                name='maps',
                url='airpollut/maps',
                controller='airpollut.controllers.maps'
            ),
            UrlMap(
                name='data',
                url='airpollut/data',
                controller='airpollut.controllers.data'
            ),
            UrlMap(
                name='about',
                url='airpollut/about',
                controller='airpollut.controllers.about'
            ),
            UrlMap(
                name='mockup',
                url='airpollut/mockup',
                controller='airpollut.controllers.mockup'
            ),
            UrlMap(
                name='proposal',
                url='airpollut/proposal',
                controller='airpollut.controllers.proposal'
            ),
            UrlMap(
                name='pollution',
                url='airpollut/pollution',
                controller='airpollut.controllers.pollution'
            ),
            UrlMap(
                name='watershed',
                url='airpollut/watershed',
                controller='airpollut.controllers.watershed'
            )
        )

        return url_maps
