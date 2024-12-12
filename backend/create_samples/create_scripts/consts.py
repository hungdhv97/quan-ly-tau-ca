import random

positions_data = [
    {
        "vessel_name": f"Tàu {chr(65 + random.randint(0, 4))}",
        "latitude": round(random.uniform(12.0, 20.0), 6),
        "longitude": round(random.uniform(110.0, 120.0), 6),
    }
    for i in range(100)
]

crew_data = [
    {
        "name": "John Doe",
        "role": "Thuyền trưởng",
        "phone": "1234567890",
        "address": "123 Đường Biển",
        "unit": "A1",
        "vessel_name": "Tàu A",
    },
    {
        "name": "Jane Smith",
        "role": "Kỹ sư",
        "phone": "9876543210",
        "address": "456 Làng Cảng",
        "unit": "B2",
        "vessel_name": "Tàu B",
    },
    {
        "name": "Sam Wilson",
        "role": "Thủy thủ",
        "phone": "5647382910",
        "address": "789 Đại lộ Bến Tàu",
        "unit": "C3",
        "vessel_name": "Tàu C",
    },
    {
        "name": "Anna Johnson",
        "role": "Đầu bếp",
        "phone": "1928374650",
        "address": "321 Đường Ven Nước",
        "unit": "D4",
        "vessel_name": "Tàu A",
    },
    {
        "name": "Lucas Brown",
        "role": "Thợ máy",
        "phone": "2938475610",
        "address": "654 Cảng Bắc",
        "unit": "E5",
        "vessel_name": "Tàu D",
    },
    {
        "name": "Emily Davis",
        "role": "Nhân viên y tế",
        "phone": "3748291056",
        "address": "987 Khu vực Trung Tâm",
        "unit": "F6",
        "vessel_name": "Tàu E",
    },
]

vessels_data = [
    {
        "name": "Tàu A",
        "imo_number": "1234567",
        "latitude": 12.34,
        "longitude": 56.78,
        "address": "Cảng A",
        "status": "Hoạt động",
        "description": "Mô tả A",
        "speed": 20.5,
    },
    {
        "name": "Tàu B",
        "imo_number": "2345678",
        "latitude": 23.45,
        "longitude": 67.89,
        "address": "Cảng B",
        "status": "Không hoạt động",
        "description": "Mô tả B",
        "speed": 30.0,
    },
    {
        "name": "Tàu C",
        "imo_number": "3456789",
        "latitude": 34.56,
        "longitude": 78.90,
        "address": "Cảng C",
        "status": "Hoạt động",
        "description": "Mô tả C",
        "speed": 15.0,
    },
    {
        "name": "Tàu D",
        "imo_number": "4567890",
        "latitude": 45.67,
        "longitude": 89.01,
        "address": "Cảng D",
        "status": "Đang bảo dưỡng",
        "description": "Mô tả D",
        "speed": 25.0,
    },
    {
        "name": "Tàu E",
        "imo_number": "5678901",
        "latitude": 56.78,
        "longitude": 90.12,
        "address": "Cảng E",
        "status": "Hoạt động",
        "description": "Mô tả E",
        "speed": 40.0,
    },
]

users_data = [
    {
        "username": "admin1",
        "password": "password123",
        "role": "admin",
        "is_active": True,
    },
    {
        "username": "crew1",
        "password": "password456",
        "role": "crew",
        "is_active": True,
    },
    {
        "username": "user1",
        "password": "password789",
        "role": "user",
        "is_active": True,
    },
    {
        "username": "admin2",
        "password": "adminpassword",
        "role": "admin",
        "is_active": True,
    },
    {
        "username": "crew2",
        "password": "password1234",
        "role": "crew",
        "is_active": False,
    },
]