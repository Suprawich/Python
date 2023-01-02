#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 00:04:00 2022

@author: karn
"""
def get_distance(address1, address2):
  address1 = int(address1.strip().replace("/",""))
  address2 = int(address2.strip().replace("/",""))
  return abs(address1-address2)

def get_sending_addresses(senders, receivers, address) :
  '''
  ฟังก์ชันนี้คืน list เก็บเลขที่บ้านทั้งหมดที่ผู้ส่งใน senders ต้องการส่งไป

  senders คือ list [ชื่อผู้ส่ง, ...]
  receivers คือ dict {ชื่อผู้ส่ง: [ชื่อผู้รับ,...] }
  address คือ dict {ชื่อ: เลขที่บ้าน}
  
  หมายเหตุ: 
    - ชื่อใดใน senders ไม่มีใน receivers ก็ข้ามชื่อนั้นไป
    - ลำดับเลขที่บ้านใน list จะเป็นอย่างไรก็ได้

	EX get_sending_addresses(['เจเจ','โมบิว'], {'เจเจ' : ['โมบิว','เอแคลร์'], 'เอแคลร์': ['กู๊ด']}, {'เจเจ' : '00/001' , 'โมบิว' : '00/011', 'เอแคลร์': '00/015', 'กู๊ด': '00/005'}) 
  จะ return ['00/011','00/015']
  '''
  house_num = []
  for sender_name in senders:
      if sender_name in receivers:
          for receiver_name in receivers[sender_name]:
              house_num.append(address[receiver_name])
  return house_num



def get_item_count(sending_addresses) :
  '''
  ฟังก์ชันนี้คืน dict {เลขที่บ้าน: จำนวนของที่ต้องส่งให้}
  โดย sending_addresses คือ list [เลขที่บ้านที่จะส่งของหนึ่งชิ้น,...]
	
  EX get_item_count(['10/000', '00/001', '00/011', '00/011', '00/009']) จะ return {'10/000' : 1, '00/001' : 1, '00/011' : 2, '00/009' : 1} 
  '''
  address_num = {}
  for address in sending_addresses:
      address_num[address] = 0
  for address in sending_addresses:
      if address in address_num:
          address_num[address] += 1
  return address_num


def calculate_fee(senders, receivers, address, discount, dispatch_center_addr) :
  '''
  ฟังก์ชันนี้คืน dict {ชื่อผู้ส่งใน sender: เงินค่าส่ง} โดยคำนวนจาก ระยะห่างของที่อยู่ผู้รับ และ dispatch_center_addr ดูวิธีคำนวณเงินค่าส่งด้านล่าง
  
  senders คือ list [ชื่อผู้ส่ง, ...]
  receivers คือ dict {ชื่อผู้ส่ง: [ชื่อผู้รับ,...] }
  address คือ dict {ชื่อ: เลขที่บ้าน}
  discount คือ dict {เกณฑ์ระยะทาง: ส่วนลดที่ได้รับเมื่อระยะทางที่ส่งจริงไม่น้อยกว่าเกณฑ์ระยะทาง}
  dispatch_center_addr คือสตริงเก็บเลขที่บ้านของศูนย์จัดส่ง เช่น '00/000'

	EX1
    senders = ['โมบิว','เอแคลร์','เจเจ']
    receivers = {'เจเจ' : ['โมบิว','เอแคลร์'], 'เอแคลร์': ['กู๊ด']}
    address = {'เจเจ' : '00/001' ,'โมบิว' : '00/011','กู๊ด':'00/005' ,'เอแคลร์': '00/015'}
    discount = {1: 0 , 3: 9, 4: 10, 8: 7}
    dispatch_center_addr = '00/000'

    ดังนั้น calculate_fee(senders, receivers, address, discount, dispatch_center_addr) จะ return dict ของค่าส่งที่ต้องจ่ายของแต่ละคน {'โมบิว' : 0, 'เอแคลร์' : 0,'เจเจ' : 61}

  จะคิดได้ดังนี้
  โดยศูนย์การจัดส่งตั้งอยู่ที่ '00/000' เราจะพิจารณาว่าเจเจส่งให้ใครบ้าง แล้วคำนวณราคาจากระยะทางตั้งแต่ศูนย์การจัดส่งถึงบ้านเลขที่ของreceiversทั้งหมด พร้อมคิดส่วนลดของระยะทางรวม
  ex. เจเจต้องส่งให้ โมบิว กับเอแคลร์ (get_distance('00/011','00/000') + get_distance('00/015','00/000')) = 26 กิโลเมตร ดังนั้นต้องจ่าย 10*2 บาท + 16*3 บาท
  และมีส่วนลด 7 บาท เนื่องจาก ไป26 กิโล เลยได้ส่วนลดของ 8 กิโล (เอากิโลที่มากที่สุดที่น้อยหรือเท่ากับกว่าค่าระยะทางนั้น)
  เจเจจะต้องจ่ายเงิน 68-7=61 บาท
  ex. เอแคลร์ต้องส่งให้ กู๊ด คือ get_distance('00/005','00/000') = 5 กิโลเมตร ดังนั้นต้องจ่าย 5*2 บาท และมีส่วนลด 10 บาท ทำให้เอแคร์ จ่ายเงิน 0 บาท
  
  หมายเหตุ - หากคิดส่วนลดแล้วมากกว่าค่าส่งจริง ให้ค่าส่งนั้นเป็น 0 บาท
          - กรณีที่ข้อมูลใน senders ไม่ปรากฏใน receivers ให้ค่าเป็น 0
  '''
  cost = {}
  distance = 0
  list_discount = [0]
  for sender_name in senders:
      cost[sender_name] = 0
      if sender_name in receivers:
          for receiver_name in receivers[sender_name]:
              distance += get_distance(address[receiver_name], dispatch_center_addr)
          if distance <= 10:
              cost[sender_name] += distance*2
          elif distance > 10:
              cost[sender_name] += 20+((distance-10)*3)
          for i in discount:
              if distance > i:
                  list_discount.append(i)
          if list_discount[len(list_discount)-1] != 0:
              cost[sender_name] -= discount[list_discount[len(list_discount)-1]]
          distance = 0
          list_discount = [0]
      if cost[sender_name] < 0:
          cost[sender_name] = 0
  return cost

def find_best_location(senders, receivers, address, discount , dispatch_centers) :
  '''
  โดยฟังก์ชั่นนี้ คืนเป็นlist ที่เก็บสองค่า ค่าแรกคือ String ชื่อที่เมื่อตั้งศูนย์การจัดส่งที่เขตนั้นจะทำให้ผลรวมของค่าส่งที่ทุกคนต้องจ่ายน้อยที่สุด
	และค่าที่สองคือ int ราคาค่าส่งทั้งหมดที่ใช้เมื่อส่งทั้งหมดของจากศูนย์การจัดส่งนั้น

  senders คือ list [ชื่อผู้ส่ง, ...]
  receivers คือ dict {ชื่อผู้ส่ง: [ชื่อผู้รับ,...] }
  address คือ dict {ชื่อ: เลขที่บ้าน}
  discount คือ dict {เกณฑ์ระยะทาง: ส่วนลดที่ได้รับเมื่อระยะทางที่ส่งจริงไม่น้อยกว่าเกณฑ์ระยะทาง}
  dispatch_centers คือ dict ที่มี key เป็น เขต และ value เป็นที่อยู่ของศูนย์การจัดส่ง {'สาธร' : '00/000', 'ร่วมฤดี' : '00/006'}

	
	EX1  
    senders = ['โมบิว','เอแคลร์','เจเจ']
    receivers = {'เจเจ' : ['โมบิว','เอแคลร์'], 'เอแคลร์': ['กู๊ด']}
    address = {'เจเจ' : '00/001' ,'โมบิว' : '00/011','กู๊ด':'00/005' ,'เอแคลร์': '00/015'}
    discount = {1: 0 , 3: 9, 4: 10, 8: 7}
    dispatch_centers = {'สาธร' : '00/000', 'ร่วมฤดี' : '00/006'}
  
    ดังนั้น find_best_location(senders, receivers, address, discount , dispatch_centers) จะ return ['ร่วมฤดี',27]

    EX2    
    senders = ['โมบิว','เอแคลร์']
    receiver = {'เจเจ' : ['โมบิว','เอแคลร์'], 'เอแคลร์': ['กู๊ด']}
    address = {'เจเจ' : '00/001' ,'โมบิว' : '00/011','กู๊ด':'00/005' ,'เอแคลร์': '00/015'}
    discount = {1: 0 , 3: 9, 4: 10, 8: 7}
    dispatch_centers = {'สาธร' : '00/000', 'ร่วมฤดี' : '00/006'}

    ดังนั้น find_best_location(senders, receivers, address, discount , dispatch_centers) จะ return ['สาธร',0]

    หมายเหตุ -หากกรณีที่ dispatch_center มีผลรวมของค่าส่งเท่ากันหลายที่ให้คืนค่าที่ dispatch_center ที่มีค่าน้อยสุดเมื่อเรียงจากพจนานุกรม(ใช้sortได้เลย)

  '''
  total = 0
  cost = []
  total_cost = {}
  compare = []
  ans = []
  for i in dispatch_centers:
      for j in calculate_fee(senders, receivers, address, discount, dispatch_centers[i]).values():
          cost.append(j)
      total = sum(cost)
      total_cost[total] = i
      cost = []
  for i in total_cost:
      compare.append(i)
  ans.append(total_cost[min(compare)])
  ans.append(min(compare))
  return ans

print(find_best_location(['โมบิว','เอแคลร์','เจเจ'], {'เจเจ' : ['โมบิว','เอแคลร์'], 'เอแคลร์': ['กู๊ด']}, {'เจเจ' : '00/001' ,'โมบิว' : '00/011','กู๊ด':'00/005' ,'เอแคลร์': '00/015'}, {1: 0 , 3: 9, 4: 10, 8: 7}, {'สาธร' : '00/000', 'ร่วมฤดี' : '00/006'}))
