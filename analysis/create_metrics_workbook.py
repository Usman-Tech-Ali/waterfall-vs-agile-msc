#!/usr/bin/env python3
"""
Create metrics.xlsx workbook with all comparison data and charts.
Run: python create_metrics_workbook.py
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, Reference, LineChart, ScatterChart
from openpyxl.chart.marker import DataPoint
import os

# Create workbook
wb = Workbook()
wb.remove(wb.active)  # Remove default sheet

# Define styles
header_fill = PatternFill(start_color="1e3a5f", end_color="1e3a5f", fill_type="solid")
header_font = Font(bold=True, color="ffffff", size=11)
alt_fill = PatternFill(start_color="f0f4f9", end_color="f0f4f9", fill_type="solid")
total_fill = PatternFill(start_color="e2e8f0", end_color="e2e8f0", fill_type="solid")
total_font = Font(bold=True)
border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

def style_header_row(ws, row_num):
    """Style a header row"""
    for cell in ws[row_num]:
        if cell.value:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            cell.border = border

def style_data_rows(ws, start_row, end_row):
    """Style data rows with alternating colors"""
    for row_idx, row in enumerate(ws.iter_rows(min_row=start_row, max_row=end_row), start=start_row):
        for cell in row:
            cell.border = border
            if (row_idx - start_row) % 2 == 0:
                cell.fill = alt_fill
            cell.alignment = Alignment(horizontal='left', vertical='center')

# ===== SHEET 1: Raw Metrics =====
ws1 = wb.create_sheet("Raw Metrics")

# Title
ws1['A1'] = "Comparative Metrics: Waterfall vs Agile"
ws1['A1'].font = Font(bold=True, size=14)
ws1.merge_cells('A1:D1')

# Metrics table
metrics_data = [
    ["Metric", "Waterfall", "Agile", "Difference"],
    ["Total development hours", 46.9, 52.5, "+5.6"],
    ["Hours: Planning/Documentation", 10.0, 7.0, "-3.0"],
    ["Hours: Coding", 14.5, 42.5, "+28.0"],
    ["Hours: Testing", 9.0, 3.0, "-6.0"],
    ["Hours: Rework (CRs)", 5.0, 8.0, "+3.0"],
    ["Total defects found", 12, 7, "-5"],
    ["High severity defects", 3, 1, "-2"],
    ["Medium severity defects", 5, 4, "-1"],
    ["Low severity defects", 4, 2, "-2"],
    ["Total defect fix effort (hrs)", 8.4, 3.1, "-5.3"],
    ["CR-001 rework hours", 2.0, 2.5, "+0.5"],
    ["CR-002 rework hours", 0.5, 1.5, "+1.0"],
    ["CR-003 rework hours", 2.5, 4.0, "+1.5"],
    ["Total CR rework hours", 5.0, 8.0, "+3.0"],
    ["Features delivered", 10, 10, "0"],
    ["Delivery rate (%)", 100, 100, "0"],
]

for row_idx, row_data in enumerate(metrics_data, start=3):
    for col_idx, value in enumerate(row_data, start=1):
        cell = ws1.cell(row=row_idx, column=col_idx, value=value)
        if row_idx == 3:
            cell.fill = header_fill
            cell.font = header_font
        elif row_idx in [8, 15]:  # Total rows
            cell.fill = total_fill
            cell.font = total_font
        cell.border = border
        if col_idx > 1:
            cell.alignment = Alignment(horizontal='center')

ws1.column_dimensions['A'].width = 35
ws1.column_dimensions['B'].width = 15
ws1.column_dimensions['C'].width = 15
ws1.column_dimensions['D'].width = 15

# ===== SHEET 2: Time Breakdown =====
ws2 = wb.create_sheet("Time Breakdown")

ws2['A1'] = "Development Hours by Phase"
ws2['A1'].font = Font(bold=True, size=14)
ws2.merge_cells('A1:D1')

time_data = [
    ["Phase", "Waterfall (hrs)", "Agile (hrs)"],
    ["Planning/Documentation", 10.0, 7.0],
    ["Coding", 14.5, 42.5],
    ["Testing", 9.0, 3.0],
    ["Rework", 13.4, 8.0],
    ["Total", 46.9, 60.5],
]

for row_idx, row_data in enumerate(time_data, start=3):
    for col_idx, value in enumerate(row_data, start=1):
        cell = ws2.cell(row=row_idx, column=col_idx, value=value)
        if row_idx == 3:
            cell.fill = header_fill
            cell.font = header_font
        elif row_idx == 8:
            cell.fill = total_fill
            cell.font = total_font
        cell.border = border
        if col_idx > 1:
            cell.alignment = Alignment(horizontal='center')

ws2.column_dimensions['A'].width = 25
ws2.column_dimensions['B'].width = 18
ws2.column_dimensions['C'].width = 18

# Add bar chart
chart = BarChart()
chart.type = "col"
chart.title = "Development Hours by Phase"
chart.y_axis.title = "Hours"
chart.x_axis.title = "Phase"

data = Reference(ws2, min_col=2, min_row=3, max_row=7, max_col=3)
cats = Reference(ws2, min_col=1, min_row=4, max_row=7)
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)
chart.height = 12
chart.width = 18

ws2.add_chart(chart, "A11")

# ===== SHEET 3: Defect Comparison =====
ws3 = wb.create_sheet("Defect Comparison")

ws3['A1'] = "Defect Detection & Fix Effort"
ws3['A1'].font = Font(bold=True, size=14)
ws3.merge_cells('A1:D1')

defect_data = [
    ["Metric", "Waterfall", "Agile"],
    ["Total defects found", 12, 7],
    ["High severity", 3, 1],
    ["Medium severity", 5, 4],
    ["Low severity", 4, 2],
    ["Total fix effort (hrs)", 8.4, 3.1],
    ["Avg fix time per defect (hrs)", 0.7, 0.44],
]

for row_idx, row_data in enumerate(defect_data, start=3):
    for col_idx, value in enumerate(row_data, start=1):
        cell = ws3.cell(row=row_idx, column=col_idx, value=value)
        if row_idx == 3:
            cell.fill = header_fill
            cell.font = header_font
        cell.border = border
        if col_idx > 1:
            cell.alignment = Alignment(horizontal='center')

ws3.column_dimensions['A'].width = 30
ws3.column_dimensions['B'].width = 15
ws3.column_dimensions['C'].width = 15

# Add bar chart
chart2 = BarChart()
chart2.type = "col"
chart2.title = "Defects Found by Methodology"
chart2.y_axis.title = "Count"

data2 = Reference(ws3, min_col=2, min_row=3, max_row=5, max_col=3)
cats2 = Reference(ws3, min_col=1, min_row=4, max_row=5)
chart2.add_data(data2, titles_from_data=True)
chart2.set_categories(cats2)
chart2.height = 12
chart2.width = 18

ws3.add_chart(chart2, "A12")

# ===== SHEET 4: Rework Comparison =====
ws4 = wb.create_sheet("Rework Comparison")

ws4['A1'] = "Rework Effort per Change Request"
ws4['A1'].font = Font(bold=True, size=14)
ws4.merge_cells('A1:D1')

rework_data = [
    ["Change Request", "Waterfall (hrs)", "Agile (hrs)", "Difference"],
    ["CR-001: Categories", 2.0, 2.5, "+0.5"],
    ["CR-002: Status Counts", 0.5, 1.5, "+1.0"],
    ["CR-003: Comments", 2.5, 4.0, "+1.5"],
    ["Total", 5.0, 8.0, "+3.0"],
]

for row_idx, row_data in enumerate(rework_data, start=3):
    for col_idx, value in enumerate(row_data, start=1):
        cell = ws4.cell(row=row_idx, column=col_idx, value=value)
        if row_idx == 3:
            cell.fill = header_fill
            cell.font = header_font
        elif row_idx == 7:
            cell.fill = total_fill
            cell.font = total_font
        cell.border = border
        if col_idx > 1:
            cell.alignment = Alignment(horizontal='center')

ws4.column_dimensions['A'].width = 25
ws4.column_dimensions['B'].width = 18
ws4.column_dimensions['C'].width = 18
ws4.column_dimensions['D'].width = 15

# Add bar chart
chart3 = BarChart()
chart3.type = "col"
chart3.title = "Rework Effort per Change Request"
chart3.y_axis.title = "Hours"

data3 = Reference(ws4, min_col=2, min_row=3, max_row=6, max_col=3)
cats3 = Reference(ws4, min_col=1, min_row=4, max_row=6)
chart3.add_data(data3, titles_from_data=True)
chart3.set_categories(cats3)
chart3.height = 12
chart3.width = 18

ws4.add_chart(chart3, "A11")

# ===== SHEET 5: Agile Burndown =====
ws5 = wb.create_sheet("Agile Burndown")

ws5['A1'] = "Agile Sprint Burndown"
ws5['A1'].font = Font(bold=True, size=14)
ws5.merge_cells('A1:D1')

burndown_data = [
    ["Day", "Sprint 1 Planned", "Sprint 1 Actual", "Sprint 2 Planned", "Sprint 2 Actual", "Sprint 3 Planned", "Sprint 3 Actual"],
    [1, 9, 9, 10, 10, 8, 8],
    [2, 8.1, 9, 9, 10, 7.2, 7],
    [3, 7.2, 7, 8, 8, 6.4, 6],
    [4, 6.3, 6, 7, 7, 5.6, 5],
    [5, 5.4, 4, 6, 5, 4.8, 4],
    [6, 4.5, 4, 5, 5, 4, 3],
    [7, 3.6, 3, 4, 3, 3.2, 2],
    [8, 2.7, 2, 3, 2, 2.4, 1],
    [9, 1.8, 1, 2, 1, 1.6, 0.5],
    [10, 0, 0, 0, 0, 0, 0],
]

for row_idx, row_data in enumerate(burndown_data, start=3):
    for col_idx, value in enumerate(row_data, start=1):
        cell = ws5.cell(row=row_idx, column=col_idx, value=value)
        if row_idx == 3:
            cell.fill = header_fill
            cell.font = header_font
        cell.border = border
        if col_idx > 1:
            cell.alignment = Alignment(horizontal='center')

ws5.column_dimensions['A'].width = 8
for col in ['B', 'C', 'D', 'E', 'F', 'G']:
    ws5.column_dimensions[col].width = 16

# Add line chart
chart4 = LineChart()
chart4.title = "Agile Sprint Burndown"
chart4.y_axis.title = "Story Points Remaining"
chart4.x_axis.title = "Day"

data4 = Reference(ws5, min_col=2, min_row=3, max_row=13, max_col=7)
cats4 = Reference(ws5, min_col=1, min_row=4, max_row=13)
chart4.add_data(data4, titles_from_data=True)
chart4.set_categories(cats4)
chart4.height = 12
chart4.width = 18

ws5.add_chart(chart4, "A16")

# ===== SHEET 6: Summary Dashboard =====
ws6 = wb.create_sheet("Summary Dashboard")

ws6['A1'] = "Methodology Comparison Summary"
ws6['A1'].font = Font(bold=True, size=16)
ws6.merge_cells('A1:C1')

# Key metrics
ws6['A3'] = "Key Metrics"
ws6['A3'].font = Font(bold=True, size=12)

summary_metrics = [
    ["", "Waterfall", "Agile"],
    ["Total Hours", 46.9, 52.5],
    ["Defects Found", 12, 7],
    ["Defect Fix Hours", 8.4, 3.1],
    ["CR Rework Hours", 5.0, 8.0],
    ["Features Delivered", 10, 10],
    ["Delivery Rate", "100%", "100%"],
]

for row_idx, row_data in enumerate(summary_metrics, start=4):
    for col_idx, value in enumerate(row_data, start=1):
        cell = ws6.cell(row=row_idx, column=col_idx, value=value)
        if row_idx == 4:
            cell.fill = header_fill
            cell.font = header_font
        cell.border = border
        if col_idx > 1:
            cell.alignment = Alignment(horizontal='center')

ws6.column_dimensions['A'].width = 20
ws6.column_dimensions['B'].width = 15
ws6.column_dimensions['C'].width = 15

# Verdict
ws6['A13'] = "Key Findings"
ws6['A13'].font = Font(bold=True, size=12)

findings = [
    "✓ Waterfall discovered 12 defects in testing phase (Week 7); Agile found 7 defects during development",
    "✓ Waterfall's late defect discovery required 8.4 hrs rework; Agile's early detection required 3.1 hrs",
    "✓ Waterfall total rework: 13.4 hrs (5 CR + 8.4 defects); Agile total rework: 8 hrs (CRs only)",
    "✓ Both methodologies achieved 100% feature delivery with identical feature sets",
    "✓ Waterfall: predictable but inflexible; Agile: flexible with continuous quality assurance",
]

for idx, finding in enumerate(findings, start=14):
    cell = ws6.cell(row=idx, column=1, value=finding)
    cell.alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
    ws6.row_dimensions[idx].height = 25

ws6.column_dimensions['A'].width = 80

# Save workbook
output_path = os.path.join(os.path.dirname(__file__), 'metrics.xlsx')
temp_path = os.path.join(os.path.dirname(__file__), 'metrics_new.xlsx')

try:
    wb.save(temp_path)
    # Try to replace the original file
    import shutil
    if os.path.exists(output_path):
        try:
            os.remove(output_path)
        except:
            pass
    shutil.move(temp_path, output_path)
    print(f"✓ Workbook created: {output_path}")
except Exception as e:
    print(f"✓ Workbook created (temp): {temp_path}")
    print(f"  Note: Original file may be locked. Please close it and run again.")
    print(f"  Error: {e}")

print(f"  - Sheet 1: Raw Metrics")
print(f"  - Sheet 2: Time Breakdown (with bar chart)")
print(f"  - Sheet 3: Defect Comparison (with bar chart)")
print(f"  - Sheet 4: Rework Comparison (with bar chart)")
print(f"  - Sheet 5: Agile Burndown (with line chart)")
print(f"  - Sheet 6: Summary Dashboard")