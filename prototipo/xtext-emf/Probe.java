import java.nio.file.*;
import java.util.*;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.*;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.util.EcoreUtil;
import org.eclipse.xtext.nodemodel.INode;
import org.eclipse.xtext.nodemodel.util.NodeModelUtils;
import org.eclipse.xtext.resource.XtextResource;
import org.eclipse.xtext.util.CancelIndicator;
import org.eclipse.xtext.validation.*;
import org.omg.kerml.xtext.KerMLStandaloneSetup;
import org.omg.sysml.xtext.SysMLStandaloneSetup;
import org.omg.sysml.io.SysMLUtil;
import org.omg.sysml.lang.sysml.*;
import com.google.inject.Injector;

public class Probe extends SysMLUtil {
  public static void main(String[] args) throws Exception {
    EPackage.Registry.INSTANCE.put(SysMLPackage.eNS_URI, SysMLPackage.eINSTANCE);
    KerMLStandaloneSetup.doSetup();
    Injector injector = new SysMLStandaloneSetup().createInjectorAndDoEMFRegistration();
    Probe p = new Probe();
    Path lib = Paths.get(args[0]).toAbsolutePath();
    Path models = Paths.get(args[1]).toAbsolutePath();
    List<Path> files;
    try (var paths = Files.walk(lib)) { files = paths.filter(Files::isRegularFile).filter(f -> f.toString().endsWith(".kerml") || f.toString().endsWith(".sysml")).sorted().toList(); }
    for (Path f : files) p.load(f, false);
    System.out.println("LIBRARY=" + files.size());
    try (var paths = Files.walk(models)) { files = paths.filter(f -> f.toString().endsWith(".sysml")).sorted().toList(); }
    for (Path f : files) p.load(f, true);
    for (Resource r: p.getInputResources()) {
      System.out.println("FILE=" + r.getURI().lastSegment());
      for (Issue i: injector.getInstance(IResourceValidator.class).validate(r, CheckMode.ALL, CancelIndicator.NullImpl))
        System.out.println("ISSUE="+i.getSeverity()+"|"+i.getCode()+"|"+i.getLineNumber()+":"+i.getColumn()+"|"+i.getMessage());
      var it = r.getAllContents();
      while(it.hasNext()) {
        EObject o = it.next();
        if(o instanceof SatisfyRequirementUsage s) System.out.println("SAT="+label(s.getSatisfiedRequirement())+"|"+label(s.getSatisfyingFeature())+"|"+loc(o));
        if(o instanceof RequirementVerificationMembership v) System.out.println("VERIFY="+label(v.getVerifiedRequirement())+"|case="+label(ownerCase(o))+"|"+loc(o));
        if(o instanceof PartUsage || o instanceof RequirementUsage || o instanceof VerificationCaseUsage) {
          Element e=(Element)o;
          if(e.getDeclaredName()!=null) System.out.println("ELEMENT="+o.eClass().getName()+"|"+e.getDeclaredName()+"|"+loc(o));
        }
      }
    }
  }
  void load(Path f, boolean input) {
    URI uri = URI.createURI(f.toUri().toASCIIString());
    Resource r = getResourceSet().getResource(uri,true);
    addResourceToIndex(r);
    if(input) addInputResource(r);
  }
  static VerificationCaseUsage ownerCase(EObject o) { for (EObject p=o.eContainer(); p!=null; p=p.eContainer()) if (p instanceof VerificationCaseUsage v) return v; return null; }
  static String label(Element e) { return e==null?"null":e.eIsProxy()?"PROXY":e.eClass().getName()+":"+e.getQualifiedName(); }
  static String loc(EObject e) { INode n=NodeModelUtils.findActualNodeFor(e); return n==null?"?":n.getStartLine()+":"+n.getOffset(); }
}
