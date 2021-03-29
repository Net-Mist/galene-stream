# Copyright (C) 2021 Alexandre Iooss
# SPDX-License-Identifier: MIT

"""
Test module for galene_rtmp.webrtc.
"""

import asyncio

from galene_rtmp.webrtc import WebRTCClient


def test_init_webrtc():
    """Test WebRTC initialization."""
    event_loop = asyncio.get_event_loop()
    client = WebRTCClient()
    client.start_pipeline(event_loop, [])
    client.close_pipeline()
