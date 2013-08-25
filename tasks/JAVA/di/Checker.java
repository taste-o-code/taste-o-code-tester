import java.io.*;
import java.lang.reflect.Method;

public class Checker {

    @DependencyInjector.Component(name = "resource")
    public static class Resource {}

    @DependencyInjector.Component(name = "bean")
    public static class Bean {
        @DependencyInjector.Inject(name = "resource")
        private Resource resource;
    }

    public boolean checkGetByClass(DependencyInjector injector) {
        injector.register(Resource.class, Bean.class);
        Bean bean = injector.getComponent(Bean.class);
        return bean.resource != null;
    }

    public boolean checkGetByName(DependencyInjector injector) {
        injector.register(Resource.class, Bean.class);
        Bean bean = (Bean) injector.getComponent("bean");
        return bean.resource != null;
    }

    public boolean checkReverseOrder(DependencyInjector injector) {
        injector.register(Bean.class, Resource.class);
        Bean bean = injector.getComponent(Bean.class);
        return bean.resource != null;
    }


    @DependencyInjector.Component(name = "nullInjection")
    public static class BeanNullInjection {

        @DependencyInjector.Inject(name = "otherResource")
        private Resource resource;
    }

    public boolean checkNullInjection(DependencyInjector injector) {
        injector.register(Resource.class, BeanNullInjection.class);
        BeanNullInjection bean = injector.getComponent(BeanNullInjection.class);
        return bean.resource == null;
    }


    public static class BeanNotComponent {

        @DependencyInjector.Inject(name = "resource")
        private Resource resource;
    }

    public boolean checkCreateWithoutComponentAnnotationOrNotRegistered(DependencyInjector injector) {
        injector.register(Resource.class);
        return injector.getComponent(Bean.class) == null
                && injector.getComponent(BeanNotComponent.class) == null;
    }



    @DependencyInjector.Component(name = "singletonResource", scope = DependencyInjector.Scope.SINGLETON)
    public static class ExplicitSingletonResource {}

    @DependencyInjector.Component(name = "explicitSinglBean", scope = DependencyInjector.Scope.SINGLETON)
    public static class BeanExplicitSingleton {

        @DependencyInjector.Inject(name = "singletonResource")
        private ExplicitSingletonResource resource;
    }


    public boolean checkSingleton(DependencyInjector injector) {
        injector.register(Resource.class, ExplicitSingletonResource.class, Bean.class, BeanExplicitSingleton.class);
        return injector.getComponent(Resource.class) == injector.getComponent(Resource.class)
                && injector.getComponent(Bean.class).resource == injector.getComponent(Bean.class).resource
                && injector.getComponent(ExplicitSingletonResource.class) == injector.getComponent(ExplicitSingletonResource.class)
                && injector.getComponent(BeanExplicitSingleton.class).resource == injector.getComponent(BeanExplicitSingleton.class).resource;
    }

    @DependencyInjector.Component(name = "prototypeResource", scope = DependencyInjector.Scope.PROTOTYPE)
    public static class PrototypeResource{}

    @DependencyInjector.Component(name = "prototypeBean", scope = DependencyInjector.Scope.PROTOTYPE)
    public static class PrototypeBean {

        @DependencyInjector.Inject(name = "resource")
        private Resource resource;

        @DependencyInjector.Inject(name = "prototypeResource")
        private PrototypeResource prototypeResource;
    }

    public boolean checkPrototype(DependencyInjector injector) {
        injector.register(Resource.class, PrototypeBean.class, PrototypeResource.class);
        PrototypeBean bean1 = injector.getComponent(PrototypeBean.class);
        PrototypeBean bean2 = injector.getComponent(PrototypeBean.class);
        return bean1 != bean2
                && bean1.prototypeResource != bean2.prototypeResource
                && bean1.resource == bean2.resource;
    }

    @DependencyInjector.Component(name = "derived")
    public static class DerivedBean extends Bean {}

    public boolean checkInheritance(DependencyInjector injector) {
        injector.register(Resource.class, DerivedBean.class);
        Bean bean = injector.getComponent(DerivedBean.class);
        return bean.resource != null;
    }

    private void run(String methodName) throws Exception {
        Method method = Checker.class.getMethod(methodName, DependencyInjector.class);
        boolean result = (Boolean) method.invoke(this, new DependencyInjector());
        System.out.println(result);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String testName = reader.readLine();
        reader.close();
        Checker checker = new Checker();
        checker.run(testName);
    }
}
