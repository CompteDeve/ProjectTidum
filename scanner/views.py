from django.shortcuts import render, get_object_or_404, redirect
from .models import ScanResult
from .forms import ScanResultForm
import subprocess
from django.contrib.auth.decorators import login_required
import os


@login_required
def scan_list(request):
    scans = ScanResult.objects.all()
    return render(request, 'scanner/scan_list.html', {'scans': scans})

@login_required
def scan_create(request):
    if request.method == "POST":
        form = ScanResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scan_list')
    else:
        form = ScanResultForm()
    return render(request, 'scanner/scan_form.html', {'form': form})

@login_required
def scan_edit(request, pk):
    scan = get_object_or_404(ScanResult, pk=pk)
    if request.method == "POST":
        form = ScanResultForm(request.POST, instance=scan)
        if form.is_valid():
            form.save()
            return redirect('scan_list')
    else:
        form = ScanResultForm(instance=scan)
    return render(request, 'scanner/scan_form.html', {'form': form})

@login_required
def scan_delete(request, pk):
    scan = get_object_or_404(ScanResult, pk=pk)
    if request.method == "POST":
        scan.delete()
        return redirect('scan_list')
    return render(request, 'scanner/scan_confirm_delete.html', {'scan': scan})


# def execute_scan(request, scan_id):
#     scan = get_object_or_404(ScanResult,id=scan_id)
#     script_path = os.path.join(os.path.dirname(__file__), "scripts/scan.sh")
#     try:
#         result = subprocess.run(["bash",script_path, scan.ip], capture_output=True, text=True, check=True)
#         scan_result = result.stdout
#     except subprocess.CalledProcessError as e:
#         scan_result = f"Erreur lors du scan : {e}"
#     return render(request, 'scanner/scan_result.html', {'scan': scan, 'scan_result': scan_result})


def execute_scan(request, scan_id):
    scan = get_object_or_404(ScanResult,id=scan_id)
    # script_path = "scripts/scan.py"
    script_path = os.path.abspath("scanner/scripts/scan.py")
    try:
        result = subprocess.run(["python",script_path, scan.ip], capture_output=True, text=True, check=True)
        scan_result = result.stdout
    except subprocess.CalledProcessError as e:
        scan_result = f"Erreur lors du scan : {e}"
    return render(request, 'scanner/scan_result.html', {'scan': scan, 'scan_result': scan_result})
