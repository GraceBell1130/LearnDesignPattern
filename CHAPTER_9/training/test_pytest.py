from tkinter import Menu
from pytest import *

from Iterator.PancakeHouseMenu import PancakeHouseMenu
from Iterator.DinerMenu import DinerMenu
from Iterator.Waitress import Waitress
from Iterator.CafeMenu import CafeMenu

def test_WaitressPrintMenu(capsys):
    pancakeHouseMenu :PancakeHouseMenu = PancakeHouseMenu()
    dinerMenu :DinerMenu = DinerMenu()
    cafeMenu :CafeMenu = CafeMenu()

    waitress :Waitress = Waitress(pancakeHouseMenu, dinerMenu, cafeMenu)
    waitress.printMenu()
    captured = capsys.readouterr()
    assert captured.out == "메뉴\n" +\
                           "----\n" +\
                           "아침메뉴\n" +\
                           "K&B 팬케이크 세트, 2.99 -- 스크램블 에그와 토스트가 곁들여진 팬케이크\n" +\
                           "레귤러 팬케이크 세트, 2.99 -- 달걀 프라이와 소시지가 곁들여진 팬케이크\n" +\
                           "블루베리 팬케이크, 3.49 -- 신선한 블루베리와 블루베리 시럽으로 만든 팬케이크\n" +\
                           "와플, 3.59 -- 취향에 따라 블루베리나 딸기를 얹을 수 있는 와플\n" +\
                           "\n점심 메뉴\n" +\
                           "채식주의자용 BLT, 2.99 -- 통밀 위에 콩고기 베이컨, 상추, 토마토를 얹은 메뉴\n" +\
                           "BLT, 2.99 -- 통밀 위에 베이컨, 상추, 토마토를 얹은 메뉴\n" +\
                           "오늘의 스프, 3.29 -- 감자 샐러드를 곁들인 오늘의 스프\n" +\
                           "핫도그, 3.05 -- 사워크라우트, 갖은 양념, 양파, 치즈가 곁들여진 핫도그\n" +\
                           "\n저녁 메뉴\n" +\
                           "베지 버거와 에어 프라이, 3.99 -- 통밀빵, 상추, 토마토, 감자 튀김이 첨가된 베지 버거\n" +\
                           "오늘의 스프, 3.69 -- 샐러드가 곁들여진 오늘의 스프\n" +\
                           "부리토, 4.29 -- 통 핀토콩과 살사, 구아카몰이 곁들여진 푸짐한 부리토\n"


from Component.MenuComponent import MenuComponent
from Component.ComponentMenu import ComponentMenu
from Component.ComponentMenuItem import ComponentMenuItem
from Component.ComponentWaitress import ComponentWaitress
def test_ComponentMenu(capsys):
    pancakeHouseMenu :MenuComponent = ComponentMenu("팬케이크 하우스 메뉴", "아침 메뉴")
    dinerMenu :MenuComponent = ComponentMenu("객체마을 식당 메뉴", "점심 메뉴")
    cafeMenu :MenuComponent = ComponentMenu("카페 메뉴", "저녁 메뉴")
    dessertMenu :MenuComponent = ComponentMenu("디저트 메뉴", "디저트를 즐겨 보세요")

    allMenus :MenuComponent = ComponentMenu("전체 메뉴", "전체 메뉴")

    allMenus.add(pancakeHouseMenu)
    pancakeHouseMenu.add(ComponentMenuItem("K&B 팬케이크 세트", "스크램블 에그와 토스트가 곁들여진 팬케이크", True, 2.99))
    pancakeHouseMenu.add(ComponentMenuItem("레귤러 팬케이크 세트", "달걀 프라이와 소시지가 곁들여진 팬케이크", False, 2.99))
    pancakeHouseMenu.add(ComponentMenuItem("블루베리 팬케이크", "신선한 블루베리와 블루베리 시럽으로 만든 팬케이크", True, 3.49))
    pancakeHouseMenu.add(ComponentMenuItem("와플", "취향에 따라 블루베리나 딸기를 얹을 수 있는 와플", True, 3.59))

    allMenus.add(dinerMenu)
    dinerMenu.add(ComponentMenuItem("채식주의자용 BLT", "통밀 위에 콩고기 베이컨, 상추, 토마토를 얹은 메뉴", True, 2.99))
    dinerMenu.add(ComponentMenuItem("BLT", "통밀 위에 베이컨, 상추, 토마토를 얹은 메뉴", False, 2.99))
    dinerMenu.add(ComponentMenuItem("오늘의 스프", "감자 샐러드를 곁들인 오늘의 스프", False, 3.29))
    dinerMenu.add(ComponentMenuItem("핫도그", "사워크라우트, 갖은 양념, 양파, 치즈가 곁들여진 핫도그", False, 3.05))
    dinerMenu.add(ComponentMenuItem("파스타", "마리나라 소스 스파게티, 효모빵도 드립니다.", True, 3.89))

    dinerMenu.add(dessertMenu)
    dessertMenu.add(ComponentMenuItem("애플 파이", "바삭바삭한 크러스트에 바닐라 아이스크림이 얹혀 있는 애플 파이", True, 1.59))
    dessertMenu.add(ComponentMenuItem("치즈케이크", "초콜릿 그레이엄 크러스트 위에 부드러운 뉴욕 치즈케이크", True, 1.99))
    dessertMenu.add(ComponentMenuItem("소르베", "라스베리와 라임의 절묘한 조화", True, 1.89))

    allMenus.add(cafeMenu)
    cafeMenu.add(ComponentMenuItem("베지 버거와 에어 프라이", "통밀빵, 상추, 토마토, 감자 튀김이 첨가된 베지 버거", True, 3.99))
    cafeMenu.add(ComponentMenuItem("오늘의 스프", "샐러드가 곁들여진 오늘의 스프", False, 3.69))
    cafeMenu.add(ComponentMenuItem("부리토", "통 핀토콩과 살사, 구아카몰이 곁들여진 푸짐한 부리토", True, 4.29))

    waitress :ComponentWaitress = ComponentWaitress(allMenus)
    waitress.printMenu()
    captured = capsys.readouterr()
    assert captured.out == "\n전체 메뉴, 전체 메뉴\n" +\
                           "--------------------\n\n" +\
                           "팬케이크 하우스 메뉴, 아침 메뉴\n" +\
                           "--------------------\n" +\
                           " K&B 팬케이크 세트(v), 2.99\n" +\
                           "    -- 스크램블 에그와 토스트가 곁들여진 팬케이크\n" +\
                           " 레귤러 팬케이크 세트, 2.99\n" +\
                           "    -- 달걀 프라이와 소시지가 곁들여진 팬케이크\n" +\
                           " 블루베리 팬케이크(v), 3.49\n" +\
                           "    -- 신선한 블루베리와 블루베리 시럽으로 만든 팬케이크\n" +\
                           " 와플(v), 3.59\n" +\
                           "    -- 취향에 따라 블루베리나 딸기를 얹을 수 있는 와플\n\n" +\
                           "객체마을 식당 메뉴, 점심 메뉴\n" +\
                           "--------------------\n" +\
                           " 채식주의자용 BLT(v), 2.99\n" +\
                           "    -- 통밀 위에 콩고기 베이컨, 상추, 토마토를 얹은 메뉴\n" +\
                           " BLT, 2.99\n" +\
                           "    -- 통밀 위에 베이컨, 상추, 토마토를 얹은 메뉴\n" +\
                           " 오늘의 스프, 3.29\n" +\
                           "    -- 감자 샐러드를 곁들인 오늘의 스프\n" +\
                           " 핫도그, 3.05\n" +\
                           "    -- 사워크라우트, 갖은 양념, 양파, 치즈가 곁들여진 핫도그\n" +\
                           " 파스타(v), 3.89\n" +\
                           "    -- 마리나라 소스 스파게티, 효모빵도 드립니다.\n\n" +\
                           "디저트 메뉴, 디저트를 즐겨 보세요\n" +\
                           "--------------------\n" +\
                           " 애플 파이(v), 1.59\n" +\
                           "    -- 바삭바삭한 크러스트에 바닐라 아이스크림이 얹혀 있는 애플 파이\n" +\
                           " 치즈케이크(v), 1.99\n" +\
                           "    -- 초콜릿 그레이엄 크러스트 위에 부드러운 뉴욕 치즈케이크\n" +\
                           " 소르베(v), 1.89\n" +\
                           "    -- 라스베리와 라임의 절묘한 조화\n\n" +\
                           "카페 메뉴, 저녁 메뉴\n" +\
                           "--------------------\n" +\
                           " 베지 버거와 에어 프라이(v), 3.99\n" +\
                           "    -- 통밀빵, 상추, 토마토, 감자 튀김이 첨가된 베지 버거\n" +\
                           " 오늘의 스프, 3.69\n" +\
                           "    -- 샐러드가 곁들여진 오늘의 스프\n" +\
                           " 부리토(v), 4.29\n" +\
                           "    -- 통 핀토콩과 살사, 구아카몰이 곁들여진 푸짐한 부리토\n"