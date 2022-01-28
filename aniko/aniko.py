from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
from aniko.data_classes import *
from aniko.error_handlers import *
import re


class Aniko:
    def __init__(
            self,
            gogoanime_token: str,
            auth_token: str, 
            host: str = "https://gogoanime.pe/"
    ):
        self.gogoanime_token = gogoanime_token
        self.auth_token = auth_token
        self.host = host

    def __str__(self) -> str:
        return "Aniko API - Copyrights (c) 2021-2025 Rohithaditya."


    def search_anime(self, query: str) -> list:
        try:
            url1 = f"{self.host}/search.html?keyword={query}"
            session = HTMLSession()
            response = session.get(url1)
            response_html = response.text
            soup = BeautifulSoup(response_html, 'html.parser')
            animes = soup.find("ul", {"class": "items"}).find_all("li")
            res_list_search = []
            for anime in animes:  # For every anime found
                tit = anime.a["title"]
                urll = anime.a["href"]
                r = urll.split('/')
                res_list_search.append(ResultObject(title=f"{tit}", animeid=f"{r[2]}"))
            if not res_list_search:
                raise NoSearchResultsError("No Search Results found for the query")
            else:
                return res_list_search
        except requests.exceptions.ConnectionError:
            raise NetworkError("Unable to connect to the Server, Check your connection")

    def get_details(self, animeid: str) -> MediaInfoObject:
        try:
            animelink = f'{self.host}category/{animeid}'
            response = requests.get(animelink)
            plainText = response.text
            soup = BeautifulSoup(plainText, "lxml")
            source_url = soup.find("div", {"class": "anime_info_body_bg"}).img
            imgg = source_url.get('src')
            tit_url = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
            lis = soup.find_all('p', {"class": "type"})
            plot_sum = lis[1]
            pl = plot_sum.get_text().split(':')
            pl.remove(pl[0])
            sum = ""
            plot_summary = sum.join(pl)
            type_of_show = lis[0].a['title']
            ai = lis[2].find_all('a')  # .find_all('title')
            genres = []
            for link in ai:
                genres.append(link.get('title'))
            year1 = lis[3].get_text()
            year2 = year1.split(" ")
            year = year2[1]
            status = lis[4].a.get_text()
            oth_names = lis[5].get_text()
            lnk = soup.find(id="episode_page")
            ep_str = str(lnk.contents[-2])
            a_tag = ep_str.split("\n")[-2]
            a_tag_sliced = a_tag[:-4].split(">")
            last_ep_range = a_tag_sliced[-1]
            y = last_ep_range.split("-")
            ep_num = y[-1]
            res_detail_search = MediaInfoObject(
                title=f"{tit_url}",
                year=int(year),
                other_names=f"{oth_names}",
                season=f"{type_of_show}",
                status=f"{status}",
                genres=genres,
                episodes=int(ep_num),
                image_url=f"{imgg}",
                summary=f"{plot_summary}"
            )
            return res_detail_search
        except AttributeError:
            raise InvalidAnimeIdError("Invalid animeid given")
        except requests.exceptions.ConnectionError:
            raise NetworkError("Unable to connect to the Server, Check your connection")

    def get_episode_link_advanced(self, animeid: str, episode_num: int) -> MediaLinksObject:
        try:
            ep_num_link_get = episode_num
            str_qry_final = animeid
            animelink = f'{self.host}category/{str_qry_final}'
            response = requests.get(animelink)
            plainText = response.text
            soup = BeautifulSoup(plainText, "lxml")
            lnk = soup.find(id="episode_page")
            source_url = lnk.find("li").a
            anime_title = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
            ep_num_tot = source_url.get("ep_end")
            last_ep = int(ep_num_tot)
            episode_url = '{}{}-episode-{}'
            url = episode_url.format(self.host, str_qry_final, ep_num_link_get)
            master_keyboard_list = []
            cookies = {
                'gogoanime': self.gogoanime_token,
                'auth': self.auth_token
            }
            response = requests.get(url=url, cookies=cookies)
            plaintext = response.text
            soup = BeautifulSoup(plaintext, "lxml")
            download_div = soup.find("div", {'class': 'cf-download'}).findAll('a')
            links_final = MediaLinksObject()
            for links in download_div:
                download_links = links['href']
                q_name_raw = links.text.strip()
                q_name_raw_list = q_name_raw.split('x')
                quality_name = q_name_raw_list[1]  # 360, 720, 1080p links .just append to keyb lists with name and href
                if quality_name == "360":
                    links_final.link_360p = download_links
                elif quality_name == "480":
                    links_final.link_480p = download_links
                elif quality_name == "720":
                    links_final.link_720p = download_links
                elif quality_name == "1080":
                    links_final.link_1080p = download_links
            anime_multi_link_initial = soup.find('div', {'class': 'anime_muti_link'}).findAll('li')
            anime_multi_link_initial.remove(anime_multi_link_initial[0])
            chumma_list = []
            for l in anime_multi_link_initial:
                get_a = l.find('a')
                video_links = get_a['data-video']
                valid = video_links[0:4]
                if valid == "http":
                    pass
                else:
                    video_links = f"https:{video_links}"
                chumma_list.append(video_links)
            anime_multi_link_initial.remove(anime_multi_link_initial[0])
            for other_links in anime_multi_link_initial:
                get_a_other = other_links.find('a')
                downlink = get_a_other['data-video']  # video links other websites
                quality_name = other_links.text.strip().split('C')[0]  # other links name quality
                if quality_name == "Streamsb":
                    links_final.link_streamsb = downlink
                elif quality_name == "Xstreamcdn":
                    links_final.link_xstreamcdn = downlink
                elif quality_name == "Streamtape":
                    links_final.link_streamtape = downlink
                elif quality_name == "Mixdrop":
                    links_final.link_mixdrop = downlink
                elif quality_name == "Mp4Upload":
                    links_final.link_mp4upload = downlink
                elif quality_name == "Doodstream":
                    links_final.link_doodstream = downlink
            res = requests.get(chumma_list[0])
            plain = res.text
            s = BeautifulSoup(plain, "lxml")
            t = s.findAll('script')
            hdp_js = t[2].string
            hdp_link_initial = re.search("(?P<url>https?://[^\s]+)", hdp_js).group("url")
            hdp_link_initial_list = hdp_link_initial.split("'")
            hdp_link_final = hdp_link_initial_list[0]  # final hdp links
            links_final.link_hdp = hdp_link_final
            return links_final
        except AttributeError:
            raise InvalidAnimeIdError("Invalid animeid or episode_num given")
        except requests.exceptions.ConnectionError:
            raise NetworkError("Unable to connect to the Server, Check your connection")
        except TypeError:
            raise InvalidTokenError("Invalid tokens passed, Check your tokens")

    def get_episode_link_basic(self, animeid: str, episode_num: int) -> MediaLinksObject():
        try:
            animelink = f'{self.host}category/{animeid}'
            response = requests.get(animelink)
            plainText = response.text
            soup = BeautifulSoup(plainText, "lxml")
            lnk = soup.find(id="episode_page")
            source_url = lnk.find("li").a
            tit_url = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
            URL_PATTERN = '{}{}-episode-{}'
            url = URL_PATTERN.format(self.host, animeid, episode_num)
            srcCode = requests.get(url)
            plainText = srcCode.text
            soup = BeautifulSoup(plainText, "lxml")
            source_url = soup.find("li", {"class": "dowloads"}).a
            vidstream_link = source_url.get('href')
            # print(vidstream_link)
            URL = vidstream_link
            dowCode = requests.get(URL)
            data = dowCode.text
            soup = BeautifulSoup(data, "lxml")
            dow_url= soup.findAll('div',{'class':'dowload'})
            episode_res_link = {'title':f"{tit_url}"}
            links_final = MediaLinksObject()
            for i in range(len(dow_url)):
                Url = dow_url[i].find('a')
                downlink = Url.get('href')
                str_= Url.string
                str_spl = str_.split()
                str_spl.remove(str_spl[0])
                str_original = ""
                quality_name = str_original.join(str_spl)
                episode_res_link.update({f"{quality_name}":f"{downlink}"})
                if "(HDP-mp4)" in quality_name:
                    links_final.link_hdp = downlink
                elif "(SDP-mp4)" in quality_name:
                    links_final.link_sdp = downlink
                elif "(360P-mp4)" in quality_name:
                    links_final.link_360p = downlink
                elif "(720P-mp4)" in quality_name:
                    links_final.link_720p = downlink
                elif "(1080P-mp4)" in quality_name:
                    links_final.link_1080p = downlink
                elif "Streamsb" in quality_name:
                    links_final.link_streamsb = downlink
                elif "Xstreamcdn" in quality_name:
                    links_final.link_xstreamcdn = downlink
                elif "Streamtape" in quality_name:
                    links_final.link_streamtape = downlink
                elif "Mixdrop" in quality_name:
                    links_final.link_mixdrop = downlink
                elif "Mp4Upload" in quality_name:
                    links_final.link_mp4upload = downlink
                elif "Doodstream" in quality_name:
                    links_final.link_doodstream = downlink
            return links_final
        except AttributeError:
            raise InvalidAnimeIdError("Invalid animeid or episode_num given")
        except requests.exceptions.ConnectionError:
            raise NetworkError("Unable to connect to the Server, Check your connection")
        except TypeError:
            raise InvalidTokenError("Invalid tokens passed, Check your tokens")            
        

    def get_by_genres(self, genre_name, page) -> list:
        try:
            url = f"{self.host}genre/{genre_name}?page={page}"
            response = requests.get(url)
            plainText = response.text
            soup = BeautifulSoup(plainText, "lxml")
            animes = soup.find("ul", {"class": "items"}).find_all("li")
            gen_ani = []
            for anime in animes:  # For every anime found
                tits = anime.a["title"]
                urll = anime.a["href"]
                r = urll.split('/')
                gen_ani.append(ResultObject(title=f"{tits}", animeid=f"{r[2]}"))
            return gen_ani
        except AttributeError or KeyError:
            raise InvalidGenreNameError("Invalid genre_name or page_num")
        except requests.exceptions.ConnectionError:
            raise NetworkError("Unable to connect to server")

    def get_airing_anime(self, count=10) -> list:
        try:
            if int(count) >= 20:
                raise CountError("count parameter cannot exceed 20")
            else:
                url = f"{self.host}"
                session = HTMLSession()
                response = session.get(url)
                response_html = response.text
                soup = BeautifulSoup(response_html, 'html.parser')
                anime = soup.find("nav", {"class": "menu_series cron"}).find("ul")
                air = []
                for link in anime.find_all('a'):
                    airing_link = link.get('href')
                    name = link.get('title')  # name of the anime
                    link = airing_link.split('/')
                    lnk_final = link[2]  # animeid of anime
                    air.append(ResultObject(title=f"{name}", animeid=f"{lnk_final}"))
                return air[0:int(count)]
        except IndexError or AttributeError or TypeError:
            raise AiringIndexError("No content found on the given page number")
        except requests.exceptions.ConnectionError:
            raise NetworkError("Unable to connect to server")