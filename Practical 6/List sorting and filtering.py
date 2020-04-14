
#Input the list
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
#Remove the maximum of the list
gene_lengths.remove(max(gene_lengths))
#Remove the minimum of the list
gene_lengths.remove(min(gene_lengths))
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
#Make the boxplot of the list, set the facecolor to be lightgreen and color to be red, set the widths to be 0.3, others are set as default.
plt.boxplot(gene_lengths, notch=None, sym=None, vert=None, 
             whis=None, positions=None, widths=0.3, 
             patch_artist=True
            , meanline=None, showmeans=None, 
             showcaps=None, showbox=None, showfliers=None, 
             boxprops={'color':'red','facecolor':'lightgreen'}, labels=None, flierprops=None, 
             medianprops=None, meanprops=None, 
             capprops=None, whiskerprops=None)
#Add the title of the boxplot
plt.title('Boxplot of gene_lengths',fontsize=22)