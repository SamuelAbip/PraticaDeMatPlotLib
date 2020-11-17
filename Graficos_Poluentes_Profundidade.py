import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
import matplotlib.lines as mlines

def mscatter(x,y,ax=None, m=None, **kw):
    import matplotlib.markers as mmarkers
    if not ax: ax=plt.gca()
    sc = ax.scatter(x,y,**kw)
    if (m is not None) and (len(m)==len(x)):
        paths = []
        for marker in m:
            if isinstance(marker, mmarkers.MarkerStyle):
                marker_obj = marker
            else:
                marker_obj = mmarkers.MarkerStyle(marker)
            path = marker_obj.get_path().transformed(
                        marker_obj.get_transform())
            paths.append(path)
        sc.set_paths(paths)
    return sc

data = """
HeavyMetals* 500 5.629849616 X
HeavyMetals* 1000    5.408656593 h
HeavyMetals* 1500    5.884519664 X
HeavyMetals* 2000    6.100197231 h
HeavyMetals*	2500	5.809141788 h
HeavyMetals*	3000	6.038920558 D
HeavyMetals*	3500	4.230805886 *
HeavyMetals*	4000	4.582201059 P
HeavyMetals*	4500	3.249596036 *
HeavyMetals*	5000	-5.066210465    *
HeavyMetals*	6000	-5.608063288    *
PCBs* 	500	2.254600818 D
PCBs* 	1000	3.937874579 D
PCBs* 	1500	2.17498928  *
PCBs* 	2000	0.837652189 *
PCBs* 	2500	-2.246416819    *
PCBs* 	3000	4.688419822 *
PCBs* 	4500	-3.568266439    *
PCBs* 	6000	-1.18183697 *
PCBs* 	10250	-0.389851072    *
PBDEs	500 2.461000814 P
PBDEs	1000  1.493355704   *
PBDEs	1500  1.761859082   *
PBDEs	2000  1.840832867   *
PBDEs	3000	1.414978359 *
PBDEs	10250	-1.540004744    *
PBHDs	500	0.87909588  *
HBCDs	500 3.850652361 *
HBCDs 1000  3.913252084 *
DDTs	500	1.942180843 D
DDTs	1000	3.372860061 D
DDTs	1500	1.898705896 *
DDTs	2000	1.102650113 *
DDTs	2500	-2.338187314    *
DDTs	3000	3.820857989 *
DDTs	4500	-5.632644079    *
HCHs*	500	2.479679546 ^
HCHs*	1000	3.004977338 ^
HCHs*	1500	-0.53153451 *
HCHs*	2000	-0.196228886    *
HCHs*	2500	-3.055517328    *
HCHs*	4500	-5.393618635    *
Organotins*	500	2.606679602 D
Organotins*	1000	3.09168633  D
Organotins*	1500	3.827635276 *
Organotins*	2000	4.404245846 P
Organotins*	2500	1.55914565  *
Organotins*	3000	0.13893394  *
Organotins*	4500	1.053517094 *
1-naphtol   1000    -0.128427064    *
1-naphtol   1500    -0.967784297    *
Phenols*	500	-0.56093812 *
Phenols*	1000	-0.859821297    *
Phenols*	1500	-0.283563374    *
Phenols*	2000	0.815551818 *
Phenols*	2500	-2.419129308    *
Phenols*	3000	-2.06694679 *
PAHs*	500	2.394391103 ^
PAHs*	1000	4.066070199 *
PAHs*	1500	2.160869146 D
PAHs*	2000	2.376127279 P
PAHs*	2500	1.274952916 *
PAHs*	3000	1.823221813 *
PAHs*	3500	2.061839477 *
PAHs*	4000	1.92116655  *
PAHs*	4500	1.691965917 *
TPHs	1500	2.924795996 *
n-alkanes	500	0.982461686 *
n-alkanes	1000	1.064809201 *
n-alkanes	1500	1.93842465  *
n-alkanes	2000	2.233678552 *
n-alkanes	2500	0.619184043 *
n-alkanes	3000	0.900367129 *
n-alkanes	3500	1.041787319 *
n-alkanes	4000	0.892094603 *
n-alkanes	4500	0.669316881 *
AHs	4500	-2.462936857    *
HCBs	500	0.837054711 ^
HCBs	1000	1.258719154 ^
HCBs	1500	-0.4308837  *
HCBs	2000	1.089361373 *
HCBs	2500	-2.954677021    *
HCBs	3000	-14.58982553    *
Fluoralsurfactants	500	3.907765962 *
Fluoralsurfactants	1000	4.832728432 P
MeO-PBDEs	500	-1.450996738    *
MHC-1	500	-1.987162775    *
Mercury	500	-0.676443691    *
Mercury	1000	-0.409696214    *
Mercury	2000	-0.434607024    *
Mercury	2500	-3.447331784    *
Mercury	3000	-3.7000571  *
Mercury	4000	-4.001087096    *
Mercury	4500	-3.447331784    *
PAEs	500	4.573911969 *
PAEs	1000	2.732394242 *
PAEs	1500	1.354108439 *
1,4-Dichlorobenzene	2000	0.279210513 *
PeCB	500	-1.566870482    *
PeCB	1000	-2.598599459    *
PeCB	1500	-3.180456064    *
PeCB	2000	-3.236572006    *
PeCB	2500	-3.638272164    *
Chlordane	500	1.653453721 *
Chlordane	1000	2.150034266 ^
Chlordane	1500	-0.207608311    *
Chlordane	2000	0.31523541  *
Herbicide	4500	2.489677304 *
AntifoulingAgentActive	1000	1.730638563 *
AntifoulingAgentActive	4500    -2.657577319    *
""".split('\n')

tlist = []
ylist = []
clist = []
dlist = []

for s in data:
    if s:
        t, y, c, d = s.split()
        y = float(y)
        c = float(c)
        tlist.append(t)
        ylist.append(y)
        clist.append(c)
        dlist.append(d)

plt.title('Pollutants per depth')
plt.xlabel("Pollutants")
plt.ylabel('Depth (m)')

scatter = mscatter(tlist, ylist, c=clist, m=dlist, s=150, cmap="jet")

plt.ylim(10500, 0)
cbar = plt.colorbar(scatter)
cbar.set_label("Concentration (μg/g)(log10)", rotation=270, labelpad=20)

incidence25 = mlines.Line2D([], [], color="black", marker="*", linestyle="None", markersize="10", label="0-49 reports")
incidence50 = mlines.Line2D([], [], color="black", marker="P", linestyle="None", markersize="10", label="50-74 reports")
incidence75 = mlines.Line2D([], [], color="black", marker="^", linestyle="None", markersize="10", label="75-99 reports")
incidence100 = mlines.Line2D([], [], color="black", marker="D", linestyle="None", markersize="10", label="100-249 reports")
incidence250 = mlines.Line2D([], [], color="black", marker="h", linestyle="None", markersize="10", label="250-499 reports")
incidence500 = mlines.Line2D([], [], color="black", marker="X", linestyle="None", markersize="10", label="500+ reports")
incidenceExplanation = mlines.Line2D([], [], color="black", marker="None", linestyle="None", markersize="10", label="* Pollutants Reported Above Maximum Allowable Concentrations (MAC-EQS)")
legend1 = plt.legend(handles=[incidence25, incidence50, incidence75, incidence100, incidence250, incidence500], title="Number of records:", bbox_to_anchor=(0.61, -0.53, 0.5, 0.5), loc='best', borderaxespad=0.)
plt.legend(handles=[incidenceExplanation], bbox_to_anchor=(0.65, -0.3), fontsize=8)
plt.gca().add_artist(legend1)

plt.xticks(rotation=90)
plt.gcf().set_size_inches(20, 10)
plt.tight_layout()
plt.show()