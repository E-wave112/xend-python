from typing import List
from xend_finance.models.schemas import Protocols

testnet_protocols = List[Protocols] = [
  {
    "name": "Venus",
    "code": "venus",
    "addresses": {
      "PROTOCOL_ADAPTER": "0xb69BF00bB8F724Bc3BfbC66A7EE423c80c303c8c",
      "PROTOCOL_SERVICE": "0x4ff202306C877841eed4d999543A916Cbde476E4",
      "GROUPS": "0x14D765A51D8765EC6eaD1A7902F314817A9f07d0",
      "CYCLES": "0x66894f6a6721c154d58DaC1FCB1ae7eD786fd5aD",
      "ESUSU_SERVICE": "0x5401F660Dd7ED429b47E3ECe4e11801229E791Ce",
      "ESUSU_STORAGE": "0xFCDb938471a16dA685c97D1f3EDd9f2C164291Bb",
      "ESUSU_ADAPTER": "0xB5fd40DC3c89361FC9E6E8dF002d2d1bC8a31fDc",
      "COOPERATIVE": "0xFb348399E414489fF7d024Aa8AfB6EB757116660",
      "PERSONAL": "0xd13dE5eD810402b26B81647f490DC47F534708cE",
      "CLIENT_RECORD": "0x0617A43dc30BaA4CF39Ad94cc0646aeD7eF23f10",
      "XEND_TOKEN": "0x4644FcaE42D96A28b8C7Ca0e7D13252e4848b817",
      "TOKEN": "0x3B7Be9D18d53cb59DCbebC6E0582DED5DF07E000",
      "PROTOCOL_CURRENCY": "VBUSD"
    }
  },
  {
    "name": "Fortube",
    "code": "fortube",
    "addresses": {
      "PROTOCOL_ADAPTER": "0x4bc6730a5e77a7f7a6dF5fbA7Df4446280657e66",
      "PROTOCOL_SERVICE": "0x7E53329e76146Fd278b2e41C12511f7AD486C8D2",
      "GROUPS": "0x405cFF755EBB3A47726f50ad30b481d1f8A02Cf4",
      "CYCLES": "0xF975dd3636c3603c097CC6EED1dff25302ad4bAa",
      "ESUSU_SERVICE": "0x42359db1d396e8b160C450C5277cA81237AfAd0d",
      "ESUSU_STORAGE": "0x9fA05476F262AF03064C45495544dCDe653E6Bb4",
      "ESUSU_ADAPTER": "0x511789A809900ac0f9f6DbcB9e194410a3B886D8",
      "COOPERATIVE": "0x37EE013a327Df57668f3A860f20A51e06E0028C8",
      "PERSONAL": "0x92Da3E991A22b415Fc8EeDD91B97cA92232421Dc",
      "CLIENT_RECORD": "0x213a8e1Fe5A74B451352d0b840f73Bb95b590C6b",
      "XEND_TOKEN": "0xa3f0c50B860E79Cef044F6aF2e8ca1ABa53D6B27",
      "TOKEN": "0x3b1F033dD955f3BE8649Cc9825A2e3E194765a3F",
      "PROTOCOL_CURRENCY": "FBUSD"
    }
  }
]