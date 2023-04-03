from _typeshed import Incomplete, ReadableBuffer, WriteableBuffer
from collections.abc import Callable
from typing import TypeVar
from typing_extensions import Literal

import _win32typing
from win32.lib.pywintypes import error as error

_T = TypeVar("_T")

def EnumFontFamilies(hdc: int, Family: str, EnumFontFamProc, Param): ...
def set_logger(logger) -> None: ...
def LOGFONT() -> _win32typing.PyLOGFONT: ...
def CreateFontIndirect(lplf: _win32typing.PyLOGFONT): ...
def GetObject(handle: int): ...
def GetObjectType(h: int): ...
def PyGetMemory(__addr: int, __len: int): ...
def PyGetString(addr, _len=...) -> str: ...
def PySetString(addr, String, maxLen): ...
def PySetMemory(addr, String): ...
def PyGetArraySignedLong(array, index): ...
def PyGetBufferAddressAndLen(obj): ...
def FlashWindow(hwnd: int, bInvert): ...
def FlashWindowEx(hwnd: int, dwFlags, uCount, dwTimeout): ...
def GetWindowLong(hwnd: int, index): ...
def GetClassLong(hwnd: int, index): ...
def SetWindowLong(hwnd: int, index, value): ...
def CallWindowProc(wndproc, hwnd: int, msg, wparam, lparam): ...
def SendMessage(
    __hwnd: int | None, __message: int, __wparam: int | None = ..., __lparam: ReadableBuffer | float | None = ...
) -> int: ...
def SendMessageTimeout(
    __hwnd: int,
    __message: int,
    __wparam: ReadableBuffer | float | None,
    __lparam: ReadableBuffer | float | None,
    __flags: int,
    __timeout: int,
) -> tuple[int, int]: ...
def PostMessage(
    __hwnd: int | None, __message: int, __wparam: int | None = ..., __lparam: ReadableBuffer | float | None = ...
) -> None: ...
def PostThreadMessage(threadId, message, wparam, lparam) -> None: ...
def ReplyMessage(result): ...
def RegisterWindowMessage(name: str): ...
def DefWindowProc(
    hwnd: int | None, message: int, wparam: ReadableBuffer | float | None, lparam: ReadableBuffer | float | None
) -> int: ...
def EnumWindows(__callback: Callable[[int, _T], object], __extra: _T) -> None: ...
def EnumThreadWindows(dwThreadId, __callback: Callable[[int, _T], object], __extra: _T) -> None: ...
def EnumChildWindows(__hwnd: int | None, __callback: Callable[[int, _T], object], __extra: _T) -> None: ...
def DialogBox(hInstance: int, TemplateName: _win32typing.PyResourceId, hWndParent: int, DialogFunc, InitParam: int = ...): ...
def DialogBoxParam(): ...
def DialogBoxIndirect(
    hInstance: int, controllist: _win32typing.PyDialogTemplate, hWndParent: int, DialogFunc, InitParam: int = ...
): ...
def DialogBoxIndirectParam(): ...
def CreateDialogIndirect(
    hInstance: int, controllist: _win32typing.PyDialogTemplate, hWndParent: int, DialogFunc, InitParam: int = ...
): ...
def EndDialog(hwnd: int, result) -> None: ...
def GetDlgItem(hDlg: int, IDDlgItem): ...
def GetDlgItemInt(hDlg: int, IDDlgItem, Signed) -> None: ...
def SetDlgItemInt(hDlg: int, IDDlgItem, Value, Signed) -> None: ...
def GetDlgCtrlID(hwnd: int): ...
def GetDlgItemText(hDlg: int, IDDlgItem) -> str: ...
def SetDlgItemText(hDlg: int, IDDlgItem, String) -> None: ...
def GetNextDlgTabItem(hDlg, hCtl, bPrevious): ...
def GetNextDlgGroupItem(hDlg, hCtl, bPrevious): ...
def SetWindowText() -> None: ...
def GetWindowText(hwnd: int) -> str: ...
def InitCommonControls() -> None: ...
def InitCommonControlsEx(flag) -> None: ...
def LoadCursor(hinstance, resid): ...
def SetCursor(hcursor): ...
def GetCursor(): ...
def GetCursorInfo() -> tuple[int, int, int, int]: ...
def CreateAcceleratorTable(accels: tuple[tuple[Incomplete, Incomplete, Incomplete], ...]): ...
def LoadMenu(hinstance, resource_id: str): ...
def DestroyMenu() -> None: ...
def SetMenu(hwnd: int, hmenu) -> None: ...
def GetMenu(__hwnd: int) -> int: ...
def LoadIcon(__hinstance: int, __resource_id_or_name: str | int) -> _win32typing.PyWNDCLASS: ...
def CopyIcon(hicon): ...
def DrawIcon(hDC, X, Y, hicon) -> None: ...
def DrawIconEx(
    hDC, xLeft, yTop, hIcon, cxWidth, cyWidth, istepIfAniCur, hbrFlickerFreeDraw: _win32typing.PyGdiHANDLE, diFlags
) -> None: ...
def CreateIconIndirect(iconinfo: _win32typing.PyICONINFO): ...
def CreateIconFromResource(bits: str, fIcon, ver: int = ...) -> int: ...
def LoadImage(
    __hinst: int, __name: str, __type: int, __cxDesired: int, __cyDesired: int, __fuLoad: int
) -> _win32typing.PyGdiHANDLE: ...
def DeleteObject(handle: _win32typing.PyGdiHANDLE) -> None: ...
def BitBlt(hdcDest, x, y, width, height, hdcSrc, nXSrc, nYSrc, dwRop) -> None: ...
def StretchBlt(hdcDest, x, y, width, height, hdcSrc, nXSrc, nYSrc, nWidthSrc, nHeightSrc, dwRop) -> None: ...
def PatBlt(hdc: int, XLeft, YLeft, Width, Height, Rop) -> None: ...
def SetStretchBltMode(hdc: int, StretchMode): ...
def GetStretchBltMode(hdc: int): ...
def TransparentBlt(
    Dest: int, XOriginDest, YOriginDest, WidthDest, HeightDest, Src: int, XOriginSrc, YOriginSrc, WidthSrc, HeightSrc, Transparent
) -> None: ...
def MaskBlt(
    Dest: int, XDest, YDest, Width, Height, Src: int, XSrc, YSrc, Mask: _win32typing.PyGdiHANDLE, xMask, yMask, Rop
) -> None: ...
def AlphaBlend(
    Dest: int,
    XOriginDest,
    YOriginDest,
    WidthDest,
    HeightDest,
    Src: int,
    XOriginSrc,
    YOriginSrc,
    WidthSrc,
    HeightSrc,
    blendFunction: _win32typing.PyBLENDFUNCTION,
) -> None: ...
def MessageBox(parent, text: str, caption: str, flags): ...
def MessageBeep(_type) -> None: ...
def CreateWindow(
    __className: str | _win32typing.PyResourceId,
    __windowTitle: str | None,
    __style: int,
    __x: int,
    __y: int,
    __width: int,
    __height: int,
    __parent: int,
    __menu: int,
    __hinstance: int,
    __reserved: Incomplete | None,
) -> int: ...
def DestroyWindow(_hwnd: int) -> None: ...
def EnableWindow(hWnd: int, bEnable): ...
def FindWindow(__ClassName: _win32typing.PyResourceId | str | None, __WindowName: str | None) -> int: ...
def FindWindowEx(
    __Parent: int | None, __ChildAfter: int | None, __ClassName: _win32typing.PyResourceId | str | None, __WindowName: str | None
) -> int: ...
def DragAcceptFiles(hwnd: int, fAccept) -> None: ...
def DragDetect(hwnd: int, point: tuple[Incomplete, Incomplete]) -> None: ...
def SetDoubleClickTime(newVal) -> None: ...
def GetDoubleClickTime(): ...
def HideCaret(hWnd: int) -> None: ...
def SetCaretPos(x, y) -> None: ...
def GetCaretPos() -> tuple[Incomplete, Incomplete]: ...
def ShowCaret(hWnd: int) -> None: ...
def ShowWindow(__hWnd: int | None, __cmdShow: int) -> int: ...
def IsWindowVisible(__hwnd: int | None) -> int: ...
def IsWindowEnabled(__hwnd: int | None) -> int: ...
def SetFocus(hwnd: int) -> None: ...
def GetFocus() -> None: ...
def UpdateWindow(__hwnd: int) -> None: ...
def BringWindowToTop(hwnd: int) -> None: ...
def SetActiveWindow(hwnd: int): ...
def GetActiveWindow(): ...
def SetForegroundWindow(__hwnd: int) -> None: ...
def GetForegroundWindow() -> int: ...
def GetClientRect(hwnd: int) -> tuple[int, int, int, int]: ...
def GetDC(hwnd: int): ...
def SaveDC(hdc: int): ...
def RestoreDC(hdc: int, SavedDC) -> None: ...
def DeleteDC(hdc) -> None: ...
def CreateCompatibleDC(dc): ...
def CreateCompatibleBitmap(hdc, width, height) -> _win32typing.PyGdiHANDLE: ...
def CreateBitmap(width, height, cPlanes, cBitsPerPixel, bitmap_bits) -> _win32typing.PyGdiHANDLE: ...
def SelectObject(hdc, _object): ...
def GetCurrentObject(hdc: int, ObjectType) -> int: ...
def GetWindowRect(hwnd: int) -> tuple[int, int, int, int]: ...
def GetStockObject(Object) -> int: ...
def PostQuitMessage(__rc: int) -> None: ...
def WaitMessage() -> None: ...
def SetWindowPos(__hWnd: int, __InsertAfter: int | None, __X: int, __Y: int, __cx: int, __cy: int, __Flags: int) -> None: ...
def GetWindowPlacement(__hwnd: int) -> tuple[int, int, tuple[int, int], tuple[int, int], tuple[int, int, int, int]]: ...
def SetWindowPlacement(hWnd: int, placement) -> None: ...
def RegisterClass(__wndClass: _win32typing.PyWNDCLASS) -> _win32typing.PyResourceId: ...
def UnregisterClass(__atom: _win32typing.PyResourceId, __hinst: int) -> None: ...
def PumpMessages() -> None: ...
def PumpWaitingMessages(__firstMessage: int = ..., __lastMessage: int = ...) -> int: ...
def GetMessage(hwnd: int, _min, _max): ...
def TranslateMessage(msg): ...
def DispatchMessage(msg): ...
def TranslateAccelerator(hwnd: int, haccel, msg): ...
def PeekMessage(hwnd: int, filterMin, filterMax, removalOptions): ...
def Shell_NotifyIcon(__Message: int, __nid: _win32typing.PyNOTIFYICONDATA) -> None: ...
def GetSystemMenu(hwnd: int, bRevert): ...
def DrawMenuBar(hwnd: int) -> None: ...
def MoveWindow(__hwnd: int, __x: int, __y: int, __width: int, __height: int, __bRepaint: bool) -> None: ...
def CloseWindow() -> None: ...
def DeleteMenu(hmenu, position, flags) -> None: ...
def RemoveMenu(hmenu, position, flags) -> None: ...
def CreateMenu(): ...
def CreatePopupMenu(): ...
def TrackPopupMenu(hmenu, flags, x, y, reserved, hwnd: int, prcRect: _win32typing.PyRECT): ...
def CommDlgExtendedError(): ...
def ExtractIcon(hinstance, moduleName: str, index): ...
def ExtractIconEx(moduleName: str, index, numIcons: int = ...): ...
def DestroyIcon(hicon) -> None: ...
def GetIconInfo(hicon: int) -> _win32typing.PyICONINFO: ...
def ScreenToClient(hWnd: int, Point: tuple[Incomplete, Incomplete]) -> tuple[Incomplete, Incomplete]: ...
def ClientToScreen(hWnd: int, Point: tuple[Incomplete, Incomplete]) -> tuple[Incomplete, Incomplete]: ...
def PaintDesktop(hdc: int) -> None: ...
def RedrawWindow(hWnd: int, rcUpdate: tuple[int, int, int, int], hrgnUpdate: _win32typing.PyGdiHANDLE, flags) -> None: ...
def GetTextExtentPoint32(hdc: int, _str: str) -> tuple[Incomplete, Incomplete]: ...
def GetTextMetrics(): ...
def GetTextCharacterExtra(hdc: int): ...
def SetTextCharacterExtra(hdc: int, CharExtra): ...
def GetTextAlign(hdc: int): ...
def SetTextAlign(hdc: int, Mode): ...
def GetTextFace(hdc: int) -> str: ...
def GetMapMode(hdc: int): ...
def SetMapMode(hdc: int, MapMode): ...
def GetGraphicsMode(hdc: int): ...
def SetGraphicsMode(hdc: int, Mode): ...
def GetLayout(hdc: int): ...
def SetLayout(hdc: int, Layout): ...
def GetPolyFillMode(hdc: int): ...
def SetPolyFillMode(hdc: int, PolyFillMode): ...
def GetWorldTransform(hdc: int) -> _win32typing.PyXFORM: ...
def SetWorldTransform(hdc: int, Xform: _win32typing.PyXFORM) -> None: ...
def ModifyWorldTransform(hdc: int, Xform: _win32typing.PyXFORM, Mode) -> None: ...
def CombineTransform(xform1: _win32typing.PyXFORM, xform2: _win32typing.PyXFORM) -> _win32typing.PyXFORM: ...
def GetWindowOrgEx(hdc: int) -> tuple[Incomplete, Incomplete]: ...
def SetWindowOrgEx(hdc: int, X, Y) -> tuple[Incomplete, Incomplete]: ...
def GetViewportOrgEx(hdc: int) -> tuple[Incomplete, Incomplete]: ...
def SetViewportOrgEx(hdc: int, X, Y) -> tuple[Incomplete, Incomplete]: ...
def GetWindowExtEx(hdc: int) -> tuple[Incomplete, Incomplete]: ...
def SetWindowExtEx(hdc: int, XExtent, YExtent) -> tuple[Incomplete, Incomplete]: ...
def GetViewportExtEx(hdc: int) -> tuple[Incomplete, Incomplete]: ...
def SetViewportExtEx(hdc: int, XExtent, YExtent) -> tuple[Incomplete, Incomplete]: ...
def GradientFill(hdc, Vertex: tuple[_win32typing.PyTRIVERTEX, ...], Mesh, Mode) -> None: ...
def GetOpenFileName(OPENFILENAME: str): ...
def InsertMenuItem(hMenu, uItem, fByPosition, menuItem) -> None: ...
def SetMenuItemInfo(hMenu, uItem, fByPosition, menuItem) -> None: ...
def GetMenuItemInfo(__hMenu: int, __uItem: int, __fByPosition: bool, __menuItem: ReadableBuffer) -> None: ...
def GetMenuItemCount(__hMenu: int | None) -> int: ...

# Actually returns a list of int|tuple, but lists don't support positional types
def GetMenuItemRect(__hWnd: int | None, __hMenu: int | None, __uItem: int) -> tuple[int, tuple[int, int, int, int]]: ...
def GetMenuState(hMenu, uID, flags): ...
def SetMenuDefaultItem(hMenu, uItem, fByPos) -> None: ...
def GetMenuDefaultItem(hMenu, fByPos, flags): ...
def AppendMenu() -> None: ...
def InsertMenu() -> None: ...
def EnableMenuItem() -> None: ...
def CheckMenuItem(): ...
def GetSubMenu(hMenu, nPos): ...
def ModifyMenu(hMnu, uPosition, uFlags, uIDNewItem, newItem: str) -> None: ...
def GetMenuItemID(hMenu, nPos): ...
def SetMenuItemBitmaps(
    hMenu, uPosition, uFlags, hBitmapUnchecked: _win32typing.PyGdiHANDLE, hBitmapChecked: _win32typing.PyGdiHANDLE
) -> None: ...
def CheckMenuRadioItem(hMenu, idFirst, idLast, idCheck, uFlags) -> None: ...
def SetMenuInfo(hmenu, info) -> None: ...
def GetMenuInfo(__hmenu: int, __info: WriteableBuffer) -> None: ...
def DrawFocusRect(hDC: int, rc: tuple[int, int, int, int]) -> None: ...
def DrawText(hDC: int, String, nCount, Rect: _win32typing.PyRECT, Format) -> tuple[Incomplete, _win32typing.PyRECT]: ...
def LineTo(hdc: int, XEnd, YEnd) -> None: ...
def Ellipse(hdc: int, LeftRect, TopRect, RightRect, BottomRect) -> None: ...
def Pie(hdc: int, LeftRect, TopRect, RightRect, BottomRect, XRadial1, YRadial1, XRadial2, YRadial2) -> None: ...
def Arc(hdc: int, LeftRect, TopRect, RightRect, BottomRect, XRadial1, YRadial1, XRadial2, YRadial2) -> None: ...
def ArcTo(hdc: int, LeftRect, TopRect, RightRect, BottomRect, XRadial1, YRadial1, XRadial2, YRadial2) -> None: ...
def AngleArc(hdc: int, Y, Y1, Radius, StartAngle: float, SweepAngle: float) -> None: ...
def Chord(hdc: int, LeftRect, TopRect, RightRect, BottomRect, XRadial1, YRadial1, XRadial2, YRadial2) -> None: ...
def ExtFloodFill(arg: int, XStart, YStart, Color, FillType) -> None: ...
def SetPixel(hdc: int, X, Y, Color): ...
def GetPixel(hdc: int, XPos, YPos): ...
def GetROP2(hdc: int): ...
def SetROP2(hdc: int, DrawMode): ...
def SetPixelV(hdc: int, X, Y, Color) -> None: ...
def MoveToEx(hdc: int, X, Y) -> tuple[Incomplete, Incomplete]: ...
def GetCurrentPositionEx(hdc: int) -> tuple[Incomplete, Incomplete]: ...
def GetArcDirection(hdc: int): ...
def SetArcDirection(hdc: int, ArcDirection): ...
def Polygon(hdc: int, Points: list[tuple[Incomplete, Incomplete]]) -> None: ...
def Polyline(hdc: int, Points: list[tuple[Incomplete, Incomplete]]) -> None: ...
def PolylineTo(hdc: int, Points: list[tuple[Incomplete, Incomplete]]) -> None: ...
def PolyBezier(hdc: int, Points: list[tuple[Incomplete, Incomplete]]) -> None: ...
def PolyBezierTo(hdc: int, Points: list[tuple[Incomplete, Incomplete]]) -> None: ...
def PlgBlt(
    Dest: int,
    Point,
    Src: int,
    XSrc,
    YSrc,
    Width,
    Height,
    Mask: _win32typing.PyGdiHANDLE | None = ...,
    xMask: int = ...,
    yMask: int = ...,
) -> None: ...
def CreatePolygonRgn(Points: list[tuple[Incomplete, Incomplete]], PolyFillMode) -> _win32typing.PyGdiHANDLE: ...
def ExtTextOut(
    hdc: int, _int, _int1, _int2, rect: _win32typing.PyRECT, string, _tuple: tuple[tuple[Incomplete, Incomplete], ...]
): ...
def GetTextColor(hdc): ...
def SetTextColor(hdc, color): ...
def GetBkMode(hdc: int): ...
def SetBkMode(hdc: int, BkMode): ...
def GetBkColor(hdc: int): ...
def SetBkColor(hdc: int, color): ...
def DrawEdge(hdc: int, rc: _win32typing.PyRECT, edge, Flags) -> _win32typing.PyRECT: ...
def FillRect(hDC: int, rc: _win32typing.PyRECT, hbr: _win32typing.PyGdiHANDLE) -> None: ...
def FillRgn(hdc: int, hrgn: _win32typing.PyGdiHANDLE, hbr: _win32typing.PyGdiHANDLE) -> None: ...
def PaintRgn(hdc: int, hrgn: _win32typing.PyGdiHANDLE) -> None: ...
def FrameRgn(hdc: int, hrgn, hbr, Width, Height) -> None: ...
def InvertRgn(hdc: int, hrgn) -> None: ...
def EqualRgn(SrcRgn1, SrcRgn2): ...
def PtInRegion(hrgn, X, Y): ...
def PtInRect(rect: tuple[int, int, int, int], point: tuple[Incomplete, Incomplete]): ...
def RectInRegion(hrgn, rc: _win32typing.PyRECT): ...
def SetRectRgn(hrgn, LeftRect, TopRect, RightRect, BottomRect) -> None: ...
def CombineRgn(Dest, Src1, Src2, CombineMode): ...
def DrawAnimatedRects(hwnd: int, idAni, minCoords: _win32typing.PyRECT, restCoords: _win32typing.PyRECT) -> None: ...
def CreateSolidBrush(Color) -> _win32typing.PyGdiHANDLE: ...
def CreatePatternBrush(hbmp: _win32typing.PyGdiHANDLE) -> _win32typing.PyGdiHANDLE: ...
def CreateHatchBrush(Style, clrref) -> _win32typing.PyGdiHANDLE: ...
def CreatePen(PenStyle, Width, Color) -> _win32typing.PyGdiHANDLE: ...
def GetSysColor(Index): ...
def GetSysColorBrush(Index) -> _win32typing.PyGdiHANDLE: ...
def InvalidateRect(hWnd: int, Rect: _win32typing.PyRECT, Erase) -> None: ...
def FrameRect(hDC: int, rc: _win32typing.PyRECT, hbr: _win32typing.PyGdiHANDLE) -> None: ...
def InvertRect(hDC: int, rc: _win32typing.PyRECT) -> None: ...
def WindowFromDC(hDC: int) -> int: ...
def GetUpdateRgn(hWnd: int, hRgn: _win32typing.PyGdiHANDLE, Erase): ...
def GetWindowRgn(hWnd: int, hRgn: _win32typing.PyGdiHANDLE): ...
def SetWindowRgn(hWnd: int, hRgn: _win32typing.PyGdiHANDLE, Redraw) -> None: ...
def ValidateRgn(hWnd: int, hRgn: _win32typing.PyGdiHANDLE) -> None: ...
def InvalidateRgn(hWnd: int, hRgn: _win32typing.PyGdiHANDLE, Erase) -> None: ...
def GetRgnBox(hrgn: _win32typing.PyGdiHANDLE) -> tuple[Incomplete, _win32typing.PyRECT]: ...
def OffsetRgn(hrgn: _win32typing.PyGdiHANDLE, XOffset, YOffset): ...
def Rectangle(hdc: int, LeftRect, TopRect, RightRect, BottomRect) -> None: ...
def RoundRect(hdc: int, LeftRect, TopRect, RightRect, BottomRect, Width, Height) -> None: ...
def BeginPaint() -> tuple[Incomplete, Incomplete]: ...
def EndPaint(hwnd: int, ps) -> None: ...
def BeginPath(hdc: int) -> None: ...
def EndPath(hdc: int) -> None: ...
def AbortPath(hdc: int) -> None: ...
def CloseFigure(hdc: int) -> None: ...
def FlattenPath(hdc: int) -> None: ...
def FillPath(hdc: int) -> None: ...
def WidenPath(hdc: int) -> None: ...
def StrokePath(hdc: int) -> None: ...
def StrokeAndFillPath(hdc: int) -> None: ...
def GetMiterLimit(hdc: int) -> float: ...
def SetMiterLimit(hdc: int, NewLimit: float) -> float: ...
def PathToRegion(hdc: int) -> _win32typing.PyGdiHANDLE: ...
def GetPath(hdc: int) -> tuple[Incomplete, Incomplete]: ...
def CreateRoundRectRgn(LeftRect, TopRect, RightRect, BottomRect, WidthEllipse, HeightEllipse): ...
def CreateRectRgnIndirect(rc: _win32typing.PyRECT): ...
def CreateEllipticRgnIndirect(rc: _win32typing.PyRECT): ...
def CreateWindowEx(
    dwExStyle, className: str, windowTitle: str, style, x, y, width, height, parent, menu, hinstance, reserved
): ...
def GetParent(child: int) -> int: ...
def SetParent(__child: int, __child1: int | None | _win32typing.PyHANDLE) -> int: ...
def GetCursorPos() -> tuple[Incomplete, Incomplete]: ...
def GetDesktopWindow(): ...
def GetWindow(__hWnd: int, __uCmd: int) -> int: ...
def GetWindowDC(hWnd: int) -> int: ...
def IsIconic(__hWnd: int) -> int: ...
def IsWindow(__hWnd: int) -> int: ...
def IsChild(__hWndParent: int, hWnd: int) -> int: ...
def ReleaseCapture() -> None: ...
def GetCapture(): ...
def SetCapture() -> None: ...
def ReleaseDC(hWnd: int, hDC): ...
def CreateCaret(hWnd: int, hBitmap: _win32typing.PyGdiHANDLE, nWidth, nHeight) -> None: ...
def DestroyCaret() -> None: ...
def ScrollWindowEx(
    hWnd: int, dx, dy, rcScroll: _win32typing.PyRECT, rcClip: _win32typing.PyRECT, hrgnUpdate, flags
) -> tuple[Incomplete, _win32typing.PyRECT]: ...
def SetScrollInfo(hwnd: int, nBar, scollInfo: _win32typing.PySCROLLINFO, bRedraw=...) -> None: ...
def GetScrollInfo(hwnd: int, nBar, mask) -> _win32typing.PySCROLLINFO: ...
def GetClassName(hwnd: int) -> str: ...
def WindowFromPoint(point: tuple[int, int]) -> int: ...
def ChildWindowFromPoint(hwndParent: int, point: tuple[Incomplete, Incomplete]): ...
def CreateDC(Driver: str, Device: str, InitData: _win32typing.PyDEVMODE): ...
def GetSaveFileNameW(
    hwndOwner: int | None = ...,
    hInstance: int | None = ...,
    Filter: Incomplete | None = ...,
    CustomFilter: Incomplete | None = ...,
    FilterIndex: int = ...,
    File: Incomplete | None = ...,
    MaxFile: int = ...,
    InitialDir: Incomplete | None = ...,
    Title: Incomplete | None = ...,
    Flags: int = ...,
    DefExt: Incomplete | None = ...,
    TemplateName: _win32typing.PyResourceId | None = ...,
) -> tuple[Incomplete, Incomplete, Incomplete]: ...
def GetOpenFileNameW(
    hwndOwner: int | None = ...,
    hInstance: int | None = ...,
    Filter: Incomplete | None = ...,
    CustomFilter: Incomplete | None = ...,
    FilterIndex: int = ...,
    File: Incomplete | None = ...,
    MaxFile: int = ...,
    InitialDir: Incomplete | None = ...,
    Title: Incomplete | None = ...,
    Flags: int = ...,
    DefExt: Incomplete | None = ...,
    TemplateName: _win32typing.PyResourceId | None = ...,
) -> tuple[Incomplete, Incomplete, Incomplete]: ...
def SystemParametersInfo(Action, Param: Incomplete | None = ..., WinIni: int = ...) -> None: ...
def SetLayeredWindowAttributes(hwnd: int, Key, Alpha, Flags) -> None: ...
def GetLayeredWindowAttributes(hwnd: int) -> tuple[Incomplete, Incomplete, Incomplete]: ...
def UpdateLayeredWindow(
    hwnd: int,
    arg: tuple[int, int, int, int],
    hdcDst: int | None = ...,
    ptDst: tuple[Incomplete, Incomplete] | None = ...,
    size: tuple[Incomplete, Incomplete] | None = ...,
    hdcSrc: Incomplete | None = ...,
    ptSrc: tuple[Incomplete, Incomplete] | None = ...,
    Key: int = ...,
    Flags: int = ...,
) -> None: ...
def AnimateWindow(hwnd: int, Time, Flags) -> None: ...
def CreateBrushIndirect(lb: _win32typing.PyLOGBRUSH) -> _win32typing.PyGdiHANDLE: ...
def ExtCreatePen(PenStyle, Width, lb: _win32typing.PyLOGBRUSH, Style: tuple[Incomplete, ...] | None = ...) -> int: ...
def DrawTextW(hDC: int, String: str, Count, Rect: _win32typing.PyRECT, Format) -> tuple[Incomplete, _win32typing.PyRECT]: ...
def EnumPropsEx(hWnd: int, EnumFunc, Param) -> None: ...
def RegisterDeviceNotification(handle: int, _filter, flags) -> _win32typing.PyHDEVNOTIFY: ...
def UnregisterDeviceNotification() -> None: ...
def RegisterHotKey(hWnd: int, _id, Modifiers, vk) -> None: ...
def GetAncestor(__hwnd: int, __gaFlags: int) -> int: ...
def GetTopWindow(__hWnd: int | None) -> int: ...
def ChildWindowFromPointEx(*args, **kwargs): ...  # incomplete
def CreateDialogIndirectParam(*args, **kwargs): ...  # incomplete
def DestroyAcceleratorTable(*args, **kwargs): ...  # incomplete
def Edit_GetLine(*args, **kwargs): ...  # incomplete
def GetModuleHandle(__lpModuleName: str | None) -> int: ...
def GetWindowTextLength(*args, **kwargs): ...  # incomplete
def HIWORD(*args, **kwargs): ...  # incomplete
def ImageList_Add(*args, **kwargs): ...  # incomplete
def ImageList_Create(*args, **kwargs): ...  # incomplete
def ImageList_Destroy(*args, **kwargs): ...  # incomplete
def ImageList_Draw(*args, **kwargs): ...  # incomplete
def ImageList_DrawEx(*args, **kwargs): ...  # incomplete
def ImageList_GetIcon(*args, **kwargs): ...  # incomplete
def ImageList_GetImageCount(*args, **kwargs): ...  # incomplete
def ImageList_LoadBitmap(*args, **kwargs): ...  # incomplete
def ImageList_LoadImage(*args, **kwargs): ...  # incomplete
def ImageList_Remove(*args, **kwargs): ...  # incomplete
def ImageList_Replace(*args, **kwargs): ...  # incomplete
def ImageList_ReplaceIcon(*args, **kwargs): ...  # incomplete
def ImageList_SetBkColor(*args, **kwargs): ...  # incomplete
def ImageList_SetOverlayImage(*args, **kwargs): ...  # incomplete
def LOWORD(*args, **kwargs): ...  # incomplete
def ListView_SortItems(*args, **kwargs): ...  # incomplete
def ListView_SortItemsEx(*args, **kwargs): ...  # incomplete
def ValidateRect(*args, **kwargs): ...  # incomplete
def WNDCLASS() -> _win32typing.PyWNDCLASS: ...
def lpstr(*args, **kwargs): ...  # incomplete

CLR_NONE: int
ILC_COLOR: int
ILC_COLOR16: int
ILC_COLOR24: int
ILC_COLOR32: int
ILC_COLOR4: int
ILC_COLOR8: int
ILC_COLORDDB: int
ILC_MASK: int
ILD_BLEND: int
ILD_BLEND25: int
ILD_BLEND50: int
ILD_FOCUS: int
ILD_MASK: int
ILD_NORMAL: int
ILD_SELECTED: int
ILD_TRANSPARENT: int
IMAGE_BITMAP: int
IMAGE_CURSOR: int
IMAGE_ICON: int
LR_CREATEDIBSECTION: int
LR_DEFAULTCOLOR: int
LR_DEFAULTSIZE: int
LR_LOADFROMFILE: int
LR_LOADMAP3DCOLORS: int
LR_LOADTRANSPARENT: int
LR_MONOCHROME: int
LR_SHARED: int
LR_VGACOLOR: int
NIF_ICON: int
NIF_INFO: int
NIF_MESSAGE: int
NIF_STATE: int
NIF_TIP: int
NIIF_ERROR: int
NIIF_ICON_MASK: int
NIIF_INFO: int
NIIF_NONE: int
NIIF_NOSOUND: int
NIIF_WARNING: int
NIM_ADD: int
NIM_DELETE: int
NIM_MODIFY: int
NIM_SETVERSION: int
TPM_BOTTOMALIGN: int
TPM_CENTERALIGN: int
TPM_LEFTALIGN: int
TPM_LEFTBUTTON: int
TPM_NONOTIFY: int
TPM_RETURNCMD: int
TPM_RIGHTALIGN: int
TPM_RIGHTBUTTON: int
TPM_TOPALIGN: int
TPM_VCENTERALIGN: int
UNICODE: Literal[True]
dllhandle: int
