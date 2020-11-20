import sys
import os

import cv2
import json

import retinex

with open('config.json', 'r') as f:
    config = json.load(f)

    img = cv2.imread("D:/3.png")

    print('msrcr processing......')
    img_msrcr = retinex.MSRCR(
        img,
        config['sigma_list'],
        config['G'],
        config['b'],
        config['alpha'],
        config['beta'],
        config['low_clip'],
        config['high_clip']
    )
    cv2.imshow('MSRCR retinex', img_msrcr)

    print('amsrcr processing......')
    img_amsrcr = retinex.automatedMSRCR(
        img,
        config['sigma_list']
    )
    cv2.imshow('autoMSRCR retinex', img_amsrcr)
    print('msrcp processing......')
    img_msrcp = retinex.MSRCP(
        img,
        config['sigma_list'],
        config['low_clip'],
        config['high_clip']
    )

    shape = img.shape
    cv2.imshow('Image', img)

    cv2.imshow('MSRCP', img_msrcp)
    cv2.imwrite('D:/autoMSRCP.png', img_amsrcr)
    cv2.imwrite('D:/MSRCPreti.png', img_msrcr)
    cv2.imwrite('D:/MSRCP.png', img_msrcp)
    cv2.waitKey()