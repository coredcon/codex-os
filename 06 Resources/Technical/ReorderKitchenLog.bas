' ============================================================
' ReorderKitchenLog — LibreOffice Basic (fast bulk version)
'
' Uses getDataArray/setDataArray for a single read + single write
' instead of cell-by-cell — runs in ~1 second regardless of row count
'
' HOW TO INSTALL:
'   1. Open LibreOffice Calc
'   2. Tools > Macros > Edit Macros
'   3. My Macros > Standard > select Standard > Insert > Module
'   4. Paste this entire file in, save
'   5. Run via Tools > Macros > Run Macro, or assign a keyboard shortcut
'      via Tools > Customize > Keyboard
' ============================================================

Sub ReorderKitchenLog()
    Dim oDoc        As Object
    Dim oSheet      As Object
    Dim oCursor     As Object
    Dim oRange      As Object
    Dim oDestRange  As Object
    Dim oCols       As Object
    Dim arrColOrder As Variant
    Dim data        As Variant
    Dim newData()   As Variant
    Dim newRow()    As Variant
    Dim headerRow   As Variant
    Dim colMap()    As Integer
    Dim nRows       As Long
    Dim nCols       As Integer
    Dim i           As Integer
    Dim j           As Integer
    Dim r           As Long

    oDoc   = ThisComponent
    oSheet = oDoc.getCurrentController().getActiveSheet()

    ' *** Three to verify: EventType, ItemID, Server
    ' If any column ends up wrong, check exact header names in your CSV
    arrColOrder = Array( _
        "Timestamp", _
        "TransactionNumber", _
        "Event", _
        "ItemDescription", _
        "Scope", _
        "ActivityLevelID", _
        "DestinationDisplayGroup", _
        "DestinationStation", _
        "DestinationView", _
        "SourceView", _
        "TransactionStartTime", _
        "CourseViewRole", _
        "CourseNumber", _
        "CourseName", _
        "CourseStartTime", _
        "CourseState", _
        "CourseType", _
        "CourseDestination", _
        "Table", _
        "CookTime1", _
        "LongestCookTime", _
        "ItemID", _
        "DepartmentNumber", _
        "ItemNumber", _
        "ParentItemNumber", _
        "CookTime2", _
        "CookTime3", _
        "CookTime4", _
        "ItemCourse", _
        "Qty", _
        "ItemType", _
        "ItemCategory", _
        "Seat", _
        "Priority", _
        "Server", _
        "ServerName", _
        "Customer", _
        "ItemDGForecastPrep", _
        "ItemViewStationID", _
        "ItemViewID", _
        "RoutingType", _
        "RoutingSchemeID", _
        "temViewFirstDisplayTime", _
        "ItemViewFirstViewedTime" _
    )

    ' Find used area bounds
    oCursor = oSheet.createCursor()
    oCursor.gotoStartOfUsedArea(False)
    oCursor.gotoEndOfUsedArea(True)
    nRows = oCursor.getRangeAddress().EndRow + 1
    nCols = oCursor.getRangeAddress().EndColumn + 1

    If nRows < 2 Or nCols < 1 Then
        MsgBox "No data found. Make sure row 1 has column headers."
        Exit Sub
    End If

    ' Read entire sheet in ONE call
    oRange = oSheet.getCellRangeByPosition(0, 0, nCols - 1, nRows - 1)
    data   = oRange.getDataArray()

    ' Map desired column names to their current column index
    headerRow = data(0)
    ReDim colMap(UBound(arrColOrder))
    For i = 0 To UBound(arrColOrder)
        colMap(i) = -1
        For j = 0 To UBound(headerRow)
            If CStr(headerRow(j)) = arrColOrder(i) Then
                colMap(i) = j
                Exit For
            End If
        Next j
    Next i

    ' Build reordered data array entirely in memory
    ReDim newData(nRows - 1)
    For r = 0 To nRows - 1
        ReDim newRow(UBound(arrColOrder))
        For i = 0 To UBound(arrColOrder)
            If colMap(i) >= 0 Then
                newRow(i) = data(r)(colMap(i))
            Else
                newRow(i) = ""
            End If
        Next i
        newData(r) = newRow
    Next r

    ' Write everything back in ONE call
    oDestRange = oSheet.getCellRangeByPosition(0, 0, UBound(arrColOrder), nRows - 1)
    oDestRange.setDataArray(newData)

    ' AutoFit columns
    oCols = oSheet.getColumns()
    For i = 0 To UBound(arrColOrder)
        oCols.getByIndex(i).OptimalWidth = True
    Next i

    ' Apply font: Calibri Bold 11pt
    oDestRange.CharFontName = "Calibri"
    oDestRange.CharHeight = 11
    oDestRange.CharWeight = com.sun.star.awt.FontWeight.BOLD

    MsgBox "Done! " & nRows - 1 & " rows reordered."
End Sub
