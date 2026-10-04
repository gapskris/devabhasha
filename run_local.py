#!/usr/bin/env python3
"""
Devabhāṣā Modern — One-Click Local Launcher
Starts a local HTTP server with native HTTP 206 Partial Content (Range requests)
and opens the browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8081

class RangeHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    HTTP request handler with native HTTP 206 Partial Content (Byte Range) support.
    Enables instant seeking, smooth scrubbing, and efficient streaming for MP4 video
    and AAC/MP3 audio in all modern browsers.
    """
    protocol_version = "HTTP/1.1"

    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            return super().send_head()

        ctype = self.guess_type(path)
        try:
            f = open(path, 'rb')
        except OSError:
            self.send_error(404, 'File not found')
            return None

        fs = os.fstat(f.fileno())
        total = fs.st_size
        range_header = self.headers.get('Range')

        if not range_header or not range_header.startswith('bytes='):
            self.send_response(200)
            self.send_header('Content-Type', ctype)
            self.send_header('Content-Length', str(total))
            self.send_header('Last-Modified', self.date_time_string(fs.st_mtime))
            self.end_headers()
            return f

        try:
            val = range_header[6:].strip()
            if ',' in val:
                f.close()
                return super().send_head()

            start_str, sep, end_str = val.partition('-')
            if not sep:
                f.close()
                return super().send_head()

            if start_str and end_str:
                start = int(start_str)
                end = int(end_str)
            elif start_str and not end_str:
                start = int(start_str)
                end = total - 1
            elif not start_str and end_str:
                length = int(end_str)
                start = max(0, total - length)
                end = total - 1
            else:
                f.close()
                return super().send_head()

            if start >= total or end >= total or start > end:
                self.send_error(416, 'Requested Range Not Satisfiable')
                self.send_header('Content-Range', f'bytes */{total}')
                self.end_headers()
                f.close()
                return None

            chunk_len = end - start + 1
            self.send_response(206)
            self.send_header('Content-Type', ctype)
            self.send_header('Content-Range', f'bytes {start}-{end}/{total}')
            self.send_header('Content-Length', str(chunk_len))
            self.send_header('Last-Modified', self.date_time_string(fs.st_mtime))
            self.end_headers()
            f.seek(start)
            return RangeFileWrapper(f, chunk_len)

        except (ValueError, TypeError):
            f.close()
            return super().send_head()

class RangeFileWrapper:
    def __init__(self, f, length):
        self.f = f
        self.remaining = length

    def read(self, size=-1):
        if self.remaining <= 0:
            return b''
        if size < 0 or size > self.remaining:
            size = self.remaining
        data = self.f.read(size)
        self.remaining -= len(data)
        return data

    def close(self):
        self.f.close()

def run():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print("=" * 65)
    print("  DEVABHĀṢĀ (1997 -> 2026) LOCAL ZERO-INSTALL LAUNCHER")
    print("=" * 65)
    print(f"  Root: {script_dir}")
    print(f"  Port: {PORT}")
    print(f"  URL:  http://localhost:{PORT}")
    print("  HTTP 206 Partial Content (Byte Range requests): ENABLED")
    print("=" * 65)
    
    server_address = ('', PORT)
    with socketserver.TCPServer(server_address, RangeHTTPRequestHandler) as httpd:
        print("Server running. Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == '__main__':
    run()
