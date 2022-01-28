class ResultObject:
    def __init__(self, title: str, animeid: str):
        self.title = title
        self.animeid = animeid

class MediaInfoObject:
    def __init__(self,
                 title: str,
                 year: int,
                 other_names: str,
                 season: str,
                 status: str,
                 genres: list,
                 episodes: int,
                 image_url: str,
                 summary: str):
        self.title = title
        self.year = year
        self.other_names = other_names
        self.season = season
        self.status = status
        self.genres = genres
        self.episodes = episodes
        self.image_url = image_url
        self.summary = summary

class MediaLinksObject:
    def __init__(self,
                 link_360p=None,
                 link_480p=None,
                 link_720p=None,
                 link_1080p=None,
                 link_hdp=None,
                 link_sdp=None,
                 link_streamsb=None,
                 link_xstreamcdn=None,
                 link_streamtape=None,
                 link_mixdrop=None,
                 link_mp4upload=None,
                 link_doodstream=None
                 ):
        self.link_360p = link_360p
        self.link_480p = link_480p
        self.link_720p = link_720p
        self.link_1080p = link_1080p
        self.link_hdp = link_hdp
        self.link_sdp = link_sdp
        self.link_streamsb = link_streamsb
        self. link_xstreamcdn = link_xstreamcdn
        self.link_streamtape = link_streamtape
        self.link_mixdrop = link_mixdrop
        self.link_mp4upload = link_mp4upload
        self.link_doodstream = link_doodstream
